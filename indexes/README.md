# Search Indexes

Generated searchable indexes live here.

Current planned non-Discord index:

`documents.sqlite`

Schema:

[../ingest/document_archive_schema.sql](../ingest/document_archive_schema.sql)

Indexes are derivative representations of the archive. They may be rebuilt.

They are never the sole surviving copy of source text, revision history, comments, or assets.

## Readable-family access index

`access/` is a generated snapshot of registry rows, evidence records, Google Sites markdown, and derived research. It is not a Discord message index. Commands and coverage rules: [../access/README.md](../access/README.md).

```bash
python -m access build
python -m access search "Golden Dawn" --project roanoke-s3
```
