"""Standing authorship policy for first-party BFDM creative sources.

Brendon Faulkner is the creator and copyright owner of this project and its
first-party creative work. That declaration is project policy. The 2026-10-09
attestation corrected one earlier batch. It is not the boundary of ownership,
and a new container does not need its own attestation.

Missing dates, paths, relationships, and revision history stay on
archival_provenance. They do not change authorship. Drive custody stays on
project_ownership_context. A specifically established collaborator or
third-party attribution is left as recorded.
"""

from __future__ import annotations

CREATOR = "Brendon Faulkner"
COPYRIGHT_OWNER = "Brendon Faulkner"
BASIS_KIND = "standing_owner_declaration"

# Live instructions and new containers must not grow these phrases back.
OBSOLETE_BOILERPLATE = (
    "not in the 2026-10-09",
    "Authorship remains UNKNOWN",
    "Default source-level authorship is `UNKNOWN`",
    "No owner attestation covers this container",
)

# Statuses that already name someone else's contribution or a mixed record.
# Do not replace these with sole Brendon authorship.
ESTABLISHED_OTHER = frozenset(
    {
        "COLLABORATIVE",
        "OTHER_AUTHOR",
        "MIXED_OR_PARTIALLY_VERIFIED",
        "MIXED_CONVERSATION_PARTIAL",
        "MIXED_ROLE_TRANSCRIPT",
    }
)

STANDING_BASIS = (
    "Standing owner declaration: Brendon Faulkner is the creator and copyright "
    "owner of first-party BFDM creative work. The 2026-10-09 attestation "
    "corrected an earlier batch. It is not the boundary of ownership. Drive "
    "custody and missing archival lineage are not authorship."
)

STANDING_SCOPE = (
    "first-party BFDM creative sources. Membership in the 2026-10-09 "
    "correction batch is not required."
)


def standing_owner_authorship(project_ownership_context: str | None = None) -> dict:
    """Authorship for a first-party container. No per-file attestation."""
    record = {
        "status": "BRENDON",
        "basis": STANDING_BASIS,
        "creator": CREATOR,
        "copyright_owner": COPYRIGHT_OWNER,
        "attribution": {
            "basis_kind": BASIS_KIND,
            "attested_by": CREATOR,
            "scope": STANDING_SCOPE,
        },
    }
    if project_ownership_context:
        record["project_ownership_context"] = project_ownership_context
    return record


def established_other(status: str | None) -> bool:
    return status in ESTABLISHED_OTHER


def container_authorship(
    status: str | None,
    basis: str | None = None,
    *,
    project_ownership_context: str | None = None,
) -> dict:
    """Choose authorship for a container being ingested.

    An explicit collaborator, other-author, or mixed status is kept.
    An existing BRENDON record with its own basis is kept.
    Missing status and UNKNOWN both take the standing declaration.
    UNKNOWN is not invented here.
    """
    if established_other(status):
        return {
            "status": status,
            "basis": basis or "Specifically established attribution. Not the standing default.",
        }
    if status == "BRENDON" and basis and "Standing owner declaration" not in basis:
        kept = {"status": "BRENDON", "basis": basis}
        if project_ownership_context:
            kept["project_ownership_context"] = project_ownership_context
        return kept
    return standing_owner_authorship(project_ownership_context)


def ingest_first_party_container(fields: dict) -> dict:
    """Build a new first-party container record.

    Does not consult the 2026-10-09 attestation report. Missing archival
    fields are recorded and do not reset authorship. A caller may pass an
    already established collaborator or third-party authorship object; that
    object is preserved.
    """
    meta = dict(fields)
    archival = dict(meta.get("archival_provenance") or {})
    unresolved = list(archival.get("unresolved_fields") or [])
    if not meta.get("original_filename") and "original_filename" not in unresolved:
        unresolved.append("original_filename")
    if unresolved and not archival.get("status"):
        archival["status"] = "PARTIAL"
    archival["unresolved_fields"] = unresolved
    archival.setdefault(
        "note",
        "Unresolved archival lineage is recorded here. It is not an authorship status.",
    )
    meta["archival_provenance"] = archival

    proposed = meta.get("authorship")
    context = None
    status = None
    basis = None
    if isinstance(proposed, dict):
        context = proposed.get("project_ownership_context")
        status = proposed.get("status")
        basis = proposed.get("basis")
    elif isinstance(proposed, str):
        status = proposed
    if established_other(status):
        meta["authorship"] = proposed if isinstance(proposed, dict) else {
            "status": status,
            "basis": basis or "Specifically established attribution. Not the standing default.",
        }
        return meta
    meta["authorship"] = standing_owner_authorship(context)
    return meta
