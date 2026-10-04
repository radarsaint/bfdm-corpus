"""Unified read API over the BFDM checkout.

This module does not ingest sources and does not search Discord message
bodies. Discord text export is owned by ``retrieval.discord_search`` on
branch ``ingest/discord-retrieval-v1``. Drive container bodies are owned
by the ``ingest/drive-project-*`` reconciliation. This layer indexes what
is already ordinary text in the checkout and reports everything it did
not search.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

FORMAT_VERSION = 1
GENERATOR = "access/1"

DEFAULT_AUTHORITIES = (
    "attributable_evidence",
    "derived_case",
    "harvest_metadata",
    "normalized_source",
    "registry",
    "relation",
    "research_note",
    "source_catalog",
    "source_metadata",
)

SKIP_RESEARCH_PREFIXES = (
    "research/kit-evaluation/",
    "research/prior-dnd-solo/",
)

DIRECTORY_PROJECTS = {
    "research/roanoke-s3": "roanoke-s3",
    "research/empire-city": "roanoke-s4",
}

FILENAME_SPANS = {
    "cryptids-s3-s4-v1.md": ("roanoke-s3", "roanoke-s4"),
    "mythic-institutions-s3-s4-v1.md": ("roanoke-s3", "roanoke-s4"),
    "roanoke-s3-to-s4-judgment-v1.md": ("roanoke-s3", "roanoke-s4"),
    "roanoke-economy-2018-to-s2.md": ("roanoke-early-2018", "roanoke-s2"),
}

CASE_JSONL = (
    "research/roanoke-s3/decision-cases-v1.jsonl",
    "research/roanoke-s3/longitudinal-decision-cases-v2.jsonl",
    "research/roanoke-s3/revision-family-v3.jsonl",
)

ID_RE = re.compile(r"\b(BCS-\d{6}|BCE-\d{6}|BCR-\d{6}|BDC-[A-Z0-9]+(?:-[A-Z0-9]+)*)\b")
EXPLICIT_MSG_RE = re.compile(r"discord-message:(\d{17,20})")
SNOW_RE = re.compile(r"(?<!\d)(\d{17,20})(?!\d)")
DATE_RE = re.compile(
    r"(?<!\d)(\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?)?)"
)


class AccessError(Exception):
    def __init__(self, message, code="error"):
        super().__init__(message)
        self.code = code


def repo_root_from(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "CORPUS_CHARTER.md").is_file() and (candidate / "registry").is_dir():
            return candidate
    raise AccessError("Not inside a bfdm-corpus checkout (no CORPUS_CHARTER.md + registry/).")


def _read_jsonl(path: Path) -> list[dict]:
    rows = []
    if not path.is_file():
        return rows
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise AccessError(f"Invalid JSONL {path}:{line_no}: {exc}") from exc
    return rows


def _fold(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    stripped = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return stripped.casefold()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sqlite_access(path: Path) -> str:
    if not path.is_file():
        return "missing"
    head = path.read_bytes()[:120]
    if head.startswith(b"SQLite format 3"):
        return "hydrated_sqlite"
    if head.startswith(b"version https://git-lfs") or b"git-lfs.github.com" in head:
        return "git_lfs_pointer"
    return "unrecognized"


def _dumps(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def make_record(**fields) -> dict:
    record = {
        "attributes": {},
        "authority": "",
        "body_status": "not_applicable",
        "captured_at": None,
        "cites": [],
        "date_end": None,
        "date_kind": None,
        "date_start": None,
        "path": "",
        "project_ids": [],
        "project_labels": [],
        "project_resolution": "none",
        "record_class": "",
        "record_id": "",
        "text": "",
        "title": "",
    }
    record.update(fields)
    record["project_ids"] = sorted({item for item in record["project_ids"] if item})
    record["project_labels"] = sorted({item for item in record["project_labels"] if item})
    record["cites"] = sorted({item for item in record["cites"] if item and item != record["record_id"]})
    record["attributes"] = json.loads(_dumps(record["attributes"]))
    return record


def _ids_in(text: str) -> list[str]:
    return ID_RE.findall(text or "")


def _explicit_messages(text: str) -> list[str]:
    return [f"discord-message:{match}" for match in EXPLICIT_MSG_RE.findall(text or "")]


def _cited_dates(text: str) -> tuple[str | None, str | None]:
    found = DATE_RE.findall(text or "")
    if not found:
        return None, None
    ordered = sorted(set(found))
    return ordered[0], ordered[-1]


def _project_for_path(rel: str) -> tuple[list[str], str]:
    for prefix, project_id in DIRECTORY_PROJECTS.items():
        if rel == prefix or rel.startswith(prefix + "/"):
            return [project_id], "directory"
    span = FILENAME_SPANS.get(Path(rel).name)
    if span:
        return list(span), "filename_span"
    return [], "none"


class Index:
    def __init__(self, repo: Path):
        self.repo = repo.resolve()
        self.records: list[dict] = []
        self.by_id: dict[str, dict] = {}
        self.manifest: dict = {}

    def output_dir(self) -> Path:
        return self.repo / "indexes" / "access"

    def records_path(self) -> Path:
        return self.output_dir() / "records.jsonl"

    def manifest_path(self) -> Path:
        return self.output_dir() / "manifest.json"


def _input_files(repo: Path) -> list[Path]:
    paths: list[Path] = []
    for folder in ("registry", "evidence"):
        root = repo / folder
        if root.is_dir():
            paths.extend(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".jsonl", ".json", ".md", ".txt"})
    sites = repo / "sources"
    if sites.is_dir():
        paths.extend(sites.rglob("pages/*.md"))
        paths.extend(sites.rglob("source.md"))
        paths.extend(sites.rglob("source.txt"))
        paths.extend(sites.rglob("metadata.json"))
        paths.extend(sites.rglob("capture.json"))
    research = repo / "research"
    if research.is_dir():
        for path in research.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(repo).as_posix()
            if rel.startswith(SKIP_RESEARCH_PREFIXES):
                continue
            if path.suffix.lower() in {".md", ".jsonl", ".json"}:
                paths.append(path)
    discord = repo / "discord"
    if discord.is_dir():
        paths.extend(discord.glob("*/README.md"))
        paths.extend(discord.glob("*/*.sqlite"))
    export_catalog = repo / "indexes" / "discord" / "catalog.json"
    if export_catalog.is_file():
        paths.append(export_catalog)
    unique = sorted({path.resolve() for path in paths if path.is_file()}, key=lambda item: item.relative_to(repo).as_posix())
    return unique


def _inputs_sha256(repo: Path, files: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in files:
        rel = path.relative_to(repo).as_posix()
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        digest.update(bytes.fromhex(_sha256_file(path)))
        digest.update(b"\n")
    return digest.hexdigest()


def _load_project_index(repo: Path) -> dict:
    projects = _read_jsonl(repo / "registry" / "projects.jsonl")
    by_id = {row["project_id"]: row for row in projects}
    names: dict[str, set[str]] = {}
    anchors: dict[str, set[str]] = {}

    def add_name(label: str, project_id: str) -> None:
        if not label:
            return
        names.setdefault(_fold(label), set()).add(project_id)

    for row in projects:
        project_id = row["project_id"]
        add_name(project_id, project_id)
        add_name(row.get("canonical_name") or "", project_id)
        add_name(row.get("title") or "", project_id)
        for alias in row.get("aliases") or []:
            if isinstance(alias, dict):
                add_name(alias.get("name") or "", project_id)
            elif isinstance(alias, str):
                add_name(alias, project_id)
        for anchor in row.get("source_anchors") or []:
            if isinstance(anchor, dict) and anchor.get("kind") == "BCS" and anchor.get("id"):
                anchors.setdefault(anchor["id"], set()).add(project_id)
    return {"by_id": by_id, "names": names, "anchors": anchors, "projects": projects}


def resolve_project(spec: str, project_index: dict) -> str:
    if spec in project_index["by_id"]:
        return spec
    hits = sorted(project_index["names"].get(_fold(spec), set()))
    if not hits:
        known = ", ".join(sorted(project_index["by_id"]))
        raise AccessError(f"Unknown project '{spec}'. Known project ids: {known}", code="unknown_project")
    if len(hits) > 1:
        raise AccessError(
            f"Project filter '{spec}' matches multiple ids: {', '.join(hits)}. Pass a project_id.",
            code="ambiguous_project",
        )
    return hits[0]


def _assign_catalog_projects(corpus_id: str, label: str, project_index: dict) -> tuple[list[str], str]:
    anchored = sorted(project_index["anchors"].get(corpus_id, set()))
    if anchored:
        return anchored, "source_anchor"
    named = sorted(project_index["names"].get(_fold(label or ""), set()))
    if len(named) == 1:
        return named, "unique_label"
    if len(named) > 1:
        return [], "ambiguous_label"
    if label:
        return [], "ambiguous_label" if _fold(label) in {"roanoke"} else "unmapped_label"
    return [], "none"
