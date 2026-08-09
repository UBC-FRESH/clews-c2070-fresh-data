# CASFRI v5 Framework Sidecar

## Identity

| Field | Value |
|-------|-------|
| Upstream repository | `https://github.com/CASFRI/CASFRI` |
| Upstream tag | `v5.3.1` |
| Upstream commit SHA-1 | `c09a70cc1f90894a1d32c2f20606430b49ae274f` |
| Tag date | 2021-08-17 |
| Framework licence | **GPL-3.0** for conversion scripts and PostgreSQL workflows |
| Curated subset licence | **CC-BY-compatible data-fact** — RFC 2 (draft) clarifies that pure data tables are not subject to copyright in Canada. The translation tables are CSV-encoded factual mappings, not creative expression. |
| Cache date | 2026-08-09 |
| Cache size | ~1.1 MB (translation tables) + 152 KB (documentation) |
| Acquisition | shallow clone via `git clone --depth 1 --branch v5.3.1 https://github.com/CASFRI/CASFRI.git` followed by selective copy of `translation/tables/` and `documentation/`. Cloned upstream was destroyed after copy to keep the data submodule sidecar narrow and to avoid vendoring GPL-3.0 framework source. |
| Currency discipline | The team's CASFRI acceptance proceeds from this snapshot. Any schema-drift during CASFRI upstream evolution must trigger a re-cache with the new tag and a SHA-1 manifest update here. |

## Contents

| Path | Source (relative to upstream root) | Bytes | Purpose |
|------|------------------------------------|-------|---------|
| `translation_tables/` | `translation/tables/` | 1,012 KB | Per-jurisdiction translation CSV. Read at runtime by `fresh_fibre.casfri_qc_reader` and `fresh_fibre.species_canonical`. Includes `qc_ini03_*`, `qc_ini04_*`, `qc_ipf05_*`, `bc_vri01_*`, plus the cross-jurisdiction `species_code_mapping.csv` and `attribute_dependencies.csv`. |
| `documentation/inventory_list_cas05.csv` | `documentation/inventory_list_cas05.csv` | 47 KB | 49-row truth table of CASFRI-supported provincial/territorial inventories. Mirrored from the upstream `documentation/`. |
| `documentation/README.md` | `documentation/specifications/README.md` | <2 KB | Pointer to the official specification document at `documentation/specifications/`. |
| `documentation/release_procedure.md` | `documentation/release_procedure.md` | <5 KB | Upstream release protocol, captured for offline reference. |
| `documentation/inventory_update_procedure.md` | `documentation/inventory_update_procedure.md` | <5 KB | Upstream inventory-update protocol. |

## What is intentionally NOT in this sidecar

- `conversion/` — Bash conversion scripts (GPL-3.0 framework source). Not vendored.
- `workflow/` — SQL/Perl/Python translation flow scripts (GPL-3.0 framework source). Not vendored.
- `helperfunctions/` — PostgreSQL helper scripts (GPL-3.0 framework source). Not vendored.
- `summary_statistics/` — R validation scripts (GPL-3.0 framework source). Not vendored.
- `translation/test/` — translation test fixtures (GPL-3.0 framework source). Not vendored.
- `docs/` — Hugo-based documentation website (data + configurations, not load-bearing for our adapter).

The adapter reads **only the translation CSV tables**, never invokes the
framework's GPL-3.0 logic. This satisfies the AGENTS.md and
`planning/casfri-v5-schema-integration-plan.md` posture: the FRESH adapter
is GPL-3.0-clean.

## Reproduction

```bash
# 1. Shallow upstream clone into a scratch directory (not part of the repo).
git clone --depth 1 --branch v5.3.1 \
  https://github.com/CASFRI/CASFRI.git /tmp/casfri_cache

# 2. Copy only the curated data subdirectory:
mkdir -p data/raw/casfri_v5/{translation_tables,documentation}
cp /tmp/casfri_cache/translation/tables/*.csv \
   data/raw/casfri_v5/translation_tables/
cp /tmp/casfri_cache/documentation/inventory_list_cas05.csv \
   /tmp/casfri_cache/documentation/release_procedure.md \
   /tmp/casfri_cache/documentation/inventory_update_procedure.md \
   /tmp/casfri_cache/documentation/specifications/README.md \
   data/raw/casfri_v5/documentation/

# 3. Verify the upstream SHA-1 matches the recorded value:
git -C /tmp/casfri_cache rev-parse HEAD \
  | diff - <(head -4 data/raw/casfri_v5/PROVENANCE.md | tail -1 | awk '{print $NF}')
```

## Acknowledgements

> CASFRI Project Team (2021). *Common Attribute Schema for Forest Resource
> Inventories*. Université Laval, QC, Canada. URL
> <https://casfri.github.io/CASFRI/>.

GPL-3.0 framework sourcecode not vendored into this project. Adapter reads
the framework's published data artefacts at runtime only.
