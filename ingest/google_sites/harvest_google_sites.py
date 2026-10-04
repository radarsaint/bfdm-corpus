#!/usr/bin/env python3
"""Harvest public Google Sites pages into BFDM source snapshots.

This is intentionally source-preserving:
- raw HTTP response HTML is retained;
- a normalized text mirror is written for search/research;
- page metadata and outbound links are recorded;
- only pages under each user-supplied Google Sites /view/<slug>/ namespace are crawled.

It does not infer that published content was played. Publication and live-delivery
remain separate evidence states.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup


UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36 "
    "BFDM-Corpus-Archiver/1.0"
)

SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "data:")
MAX_PAGES_PER_SITE = 250


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def canonicalize(url: str) -> str:
    p = urlsplit(url)
    path = re.sub(r"/+", "/", p.path)
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), path, "", ""))


def safe_name(url: str, site_prefix: str) -> str:
    path = urlsplit(url).path
    prefix_path = urlsplit(site_prefix).path.rstrip("/")
    rel = path[len(prefix_path):].strip("/") if path.startswith(prefix_path) else path.strip("/")
    if not rel:
        rel = "home"
    rel = re.sub(r"[^A-Za-z0-9._-]+", "__", rel)
    rel = rel.strip("._-") or "home"
    if len(rel) > 140:
        rel = rel[:100] + "__" + hashlib.sha256(url.encode()).hexdigest()[:16]
    return rel


def text_from_html(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    title = ""
    if soup.title and soup.title.get_text(strip=True):
        title = soup.title.get_text(" ", strip=True)

    for tag in soup(["script", "style", "noscript", "svg", "template"]):
        tag.decompose()

    main = soup.find("main") or soup.body or soup
    lines = []
    last = None
    for s in main.stripped_strings:
        s = re.sub(r"\s+", " ", s).strip()
        if not s or s == last:
            continue
        if s in {"Skip to main content", "Skip to navigation", "Search this site"}:
            continue
        lines.append(s)
        last = s
    return title, "\n\n".join(lines).strip() + "\n"


def page_links(html: str, page_url: str, root_prefix: str) -> tuple[list[str], list[str], list[str]]:
    soup = BeautifulSoup(html, "html.parser")
    root = canonicalize(root_prefix).rstrip("/") + "/"
    all_links = set()
    same_site = set()
    drive_links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if not href or href.startswith(SKIP_SCHEMES) or href.startswith("#"):
            continue
        target = canonicalize(urljoin(page_url, href))
        all_links.add(target)
        if target.startswith(root):
            same_site.add(target)
        host = urlsplit(target).netloc.lower()
        if host in {"drive.google.com", "docs.google.com"}:
            drive_links.add(target)
    return sorted(all_links), sorted(same_site), sorted(drive_links)


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def harvest_site(session: requests.Session, site: dict, root: Path) -> dict:
    slug = site["slug"]
    start = canonicalize(site["url"])
    root_prefix = f"https://sites.google.com/view/{slug}/"
    site_dir = root / slug
    raw_dir = site_dir / "raw"
    page_dir = site_dir / "pages"
    raw_dir.mkdir(parents=True, exist_ok=True)
    page_dir.mkdir(parents=True, exist_ok=True)

    queue = deque([start])
    seen = set()
    records = []
    failures = []

    while queue and len(seen) < MAX_PAGES_PER_SITE:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)
        fetched_at = utcnow()
        rec = {
            "url": url,
            "fetched_at": fetched_at,
            "http_status": None,
            "final_url": None,
            "title": None,
            "raw_path": None,
            "text_path": None,
            "sha256_html": None,
            "sha256_text": None,
            "links_all": [],
            "links_same_site": [],
            "google_drive_links": [],
            "error": None,
        }
        try:
            resp = session.get(url, timeout=35, allow_redirects=True)
            rec["http_status"] = resp.status_code
            rec["final_url"] = canonicalize(resp.url)
            resp.raise_for_status()
            html = resp.text
            title, text = text_from_html(html)
            all_links, links, drive_links = page_links(html, resp.url, root_prefix)
            rec["title"] = title
            rec["links_all"] = all_links
            rec["links_same_site"] = links
            rec["google_drive_links"] = drive_links

            stem = safe_name(url, root_prefix)
            raw_path = raw_dir / f"{stem}.html"
            text_path = page_dir / f"{stem}.md"
            raw_path.write_text(html, encoding=resp.encoding or "utf-8", errors="replace")
            header = (
                f"# {title or slug}\n\n"
                f"- Source URL: {url}\n"
                f"- Final URL: {rec['final_url']}\n"
                f"- Retrieved: {fetched_at}\n"
                f"- Project: roanoke-s5-legends\n"
                f"- Evidence state: PUBLISHED_PLAYER_FACING_SOURCE\n\n"
                "---\n\n"
            )
            text_path.write_text(header + text, encoding="utf-8")
            rec["raw_path"] = raw_path.as_posix()
            rec["text_path"] = text_path.as_posix()
            rec["sha256_html"] = hashlib.sha256(html.encode("utf-8", errors="replace")).hexdigest()
            rec["sha256_text"] = hashlib.sha256(text.encode("utf-8")).hexdigest()

            for link in links:
                if link not in seen and link not in queue:
                    queue.append(link)
        except Exception as exc:
            rec["error"] = f"{type(exc).__name__}: {exc}"
            failures.append({"url": url, "error": rec["error"]})
        records.append(rec)
        time.sleep(0.15)

    status = "CAPTURED" if any(r["http_status"] == 200 and r["text_path"] for r in records) else "FAILED"
    if queue:
        status = "PARTIAL_PAGE_LIMIT"

    metadata = {
        "schema_version": "bfdm_google_site_capture/v1",
        "project_id": "roanoke-s5-legends",
        "source_family": "season-5-google-sites",
        "site_slug": slug,
        "seed_url": site["url"],
        "role": site.get("role"),
        "capture_started_from": start,
        "captured_at": utcnow(),
        "status": status,
        "page_count_attempted": len(records),
        "page_count_captured": sum(1 for r in records if r["text_path"]),
        "failure_count": len(failures),
        "page_limit": MAX_PAGES_PER_SITE,
        "pages": records,
        "limitations": [
            "Snapshot covers public HTTP content reachable from the supplied Google Sites namespace at capture time.",
            "Google Drive/Docs links exposed in page anchors are recorded but are not automatically treated as duplicate source bodies.",
            "Publication is evidence of player-facing implementation state, not proof of live use."
        ]
    }
    write_json(site_dir / "metadata.json", metadata)

    readme = [
        f"# {slug}",
        "",
        f"- Seed URL: {site['url']}",
        f"- Preliminary role: {site.get('role','')}",
        f"- Capture status: {status}",
        f"- Pages captured: {metadata['page_count_captured']} / {metadata['page_count_attempted']}",
        f"- Failures: {metadata['failure_count']}",
        "",
        "Raw HTTP HTML is under raw/; normalized readable mirrors are under pages/.",
        "See metadata.json for page-level URLs, hashes, retrieval timestamps, and link graph.",
        "",
        "Evidence note: this is published/player-facing material. It must not be silently upgraded to proof that the material was actually used in live play.",
        ""
    ]
    (site_dir / "README.md").write_text("\n".join(readme), encoding="utf-8")
    return metadata


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="ingest/google_sites/season5_sites.json")
    ap.add_argument("--output", default="sources/roanoke-s5-legends/google-sites")
    ap.add_argument("--report-prefix", default="ingest/reports/2026-10-04-season5-google-sites")
    args = ap.parse_args()

    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({
        "User-Agent": UA,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    })

    results = []
    for site in manifest["sites"]:
        print(f"[harvest] {site['slug']} {site['url']}", flush=True)
        results.append(harvest_site(session, site, output))

    summary = {
        "schema_version": "bfdm_google_sites_harvest_report/v1",
        "project_id": manifest["project_id"],
        "source_family": manifest["source_family"],
        "completed_at": utcnow(),
        "site_count": len(results),
        "sites_captured": sum(1 for r in results if r["page_count_captured"] > 0),
        "sites_failed": sum(1 for r in results if r["page_count_captured"] == 0),
        "pages_attempted": sum(r["page_count_attempted"] for r in results),
        "pages_captured": sum(r["page_count_captured"] for r in results),
        "failures": sum(r["failure_count"] for r in results),
        "sites": [
            {
                "site_slug": r["site_slug"],
                "seed_url": r["seed_url"],
                "role": r["role"],
                "status": r["status"],
                "page_count_attempted": r["page_count_attempted"],
                "page_count_captured": r["page_count_captured"],
                "failure_count": r["failure_count"]
            }
            for r in results
        ]
    }
    report_json = Path(args.report_prefix + ".json")
    report_md = Path(args.report_prefix + ".md")
    write_json(report_json, summary)

    rows = [
        "# Season 5 Google Sites harvest report",
        "",
        f"- Completed: {summary['completed_at']}",
        f"- Sites in manifest: {summary['site_count']}",
        f"- Sites with at least one captured page: {summary['sites_captured']}",
        f"- Sites with zero captured pages: {summary['sites_failed']}",
        f"- Pages captured: {summary['pages_captured']} / {summary['pages_attempted']}",
        f"- Fetch failures: {summary['failures']}",
        "",
        "| Site | Status | Pages captured | Failures | Role |",
        "|---|---:|---:|---:|---|"
    ]
    for r in summary["sites"]:
        rows.append(
            f"| {r['site_slug']} | {r['status']} | "
            f"{r['page_count_captured']}/{r['page_count_attempted']} | "
            f"{r['failure_count']} | {r['role']} |"
        )
    rows += [
        "",
        "## Evidence boundary",
        "",
        "These snapshots establish a published/player-facing implementation state. "
        "They do not establish that every published rule, class, item, background, "
        "or page was used in live Season 5 play.",
        ""
    ]
    report_md.parent.mkdir(parents=True, exist_ok=True)
    report_md.write_text("\n".join(rows), encoding="utf-8")

    print(json.dumps(summary, indent=2))
    return 0 if summary["sites_captured"] else 2


if __name__ == "__main__":
    sys.exit(main())
