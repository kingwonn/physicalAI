# tools/ — HTML build scripts

Deliverable builders (run with python3; they read `wiki/`/`wiki-zh/` and write
HTML to the session scratchpad — copy outputs into `docs/`):

- `build_reader.py` — single-file English reader (docs/reader-en.html)
- `build_reader_zh.py` — single-file Chinese reader (docs/reader-zh.html)
- `build_dataengine.py` — data-engine roadmap visual (docs/data-engine-roadmap.html)

Committed to the repo after a tmp cleanup wiped the scratchpad copies
(recovered via transcript Write/Edit replay, 2026-07-07). When adding a wiki
page, add it to GROUPS in both reader scripts. Output paths (BASE/OUT) are
absolute to the current session scratchpad — adjust when the session changes.
