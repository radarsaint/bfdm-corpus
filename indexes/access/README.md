# Access index

Generated snapshot of the readable corpus. Not a canonical source.

- `records.jsonl` — one access record per line. Schema and commands: [../../access/README.md](../../access/README.md).
- `manifest.json` — format version, record counts, and `inputs_sha256`.

Rebuild after source changes:

```bash
python -m access build
```

Query commands rebuild automatically when the input hash no longer matches.
Discord message text is not in this index.
