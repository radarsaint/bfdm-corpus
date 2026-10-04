"""Unified read API over the BFDM checkout.

The implementation is split across model, report, build, and commands so each
file can be published through a size-limited file API. Import from here.
"""

from access.build import build_index
from access.commands import (
    audit,
    coverage,
    entity,
    evidence,
    export_bundle,
    main,
    record,
    related,
    search,
    sources,
    timeline,
)
from access.model import AccessError, repo_root_from, resolve_project
from access.report import assess_database_access

__all__ = [
    "AccessError",
    "assess_database_access",
    "audit",
    "build_index",
    "coverage",
    "entity",
    "evidence",
    "export_bundle",
    "main",
    "record",
    "related",
    "repo_root_from",
    "resolve_project",
    "search",
    "sources",
    "timeline",
]
