# Search Indexes

Generated searchable indexes live here.

Current planned non-Discord index:

`documents.sqlite`

Schema:

[../ingest/document_archive_schema.sql](../ingest/document_archive_schema.sql)

Indexes are derivative representations of the archive. They may be rebuilt.

They are never the sole surviving copy of source text, revision history, comments, or assets.

## Discord retrieval

`discord/` contains deterministic ordinary-text shards, token postings, scoped alias links, source hashes, and checksums. These are readable through GitHub file tools without LFS or a hosted search service. Use [../retrieval/README.md](../retrieval/README.md) for model instructions and commands. The generated FTS search database is an ignored local cache, rebuilt from these shards.
