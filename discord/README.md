# Discord harvests

One folder per server: `discord/<server-slug>/` containing `<server-slug>.sqlite` and a `README.md`
(server name, server ID, campaigns played there, date range, channels included, harvest date),
plus an `attachments/` folder holding every downloaded attachment file.
Every database follows [SCHEMA.md](SCHEMA.md). Re-harvests replace the existing database.

For GitHub/model retrieval without opening the LFS databases, use [../retrieval/README.md](../retrieval/README.md) and the generated [catalog](../indexes/discord/catalog.json). Historical private-source labels are subject to the current owner access decision in the root README.
