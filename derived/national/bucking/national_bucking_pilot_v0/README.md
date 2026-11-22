# National bucking pilot v0 — Quebec

**Scope: pilot.**  This directory is a Phase 0/2 pilot for one non-BC
jurisdiction (Quebec).  It is not a national supply estimate, not an
operational grade recovery, and not a validation of the taper outside its
published Quebec domain.

## What ran

1. A 24-tree synthetic Quebec tree list (`tree_list.csv`).  Species, DBH and
   height are hand-authored for contract testing; every row says
   `synthetic_pilot_v0` and `assumption`.
2. The published Schneider (2013) fixed-effect tree taper for eight Quebec
   species (`taper_registry.csv`), implemented in
   `workflows/national/bucking/schneider2013.py` from the CFSForestTools
   parameter tables (LGPL-3.0).  Every log records `taper_evidence`.
3. A pilot dimension-only sort rule set (`grade_rules.csv`).  It is informed by
   Quebec MERIS/Petro product dimensions but is **not** an official Quebec log
   grade.  `grade=not_assigned` and `sort_basis=dimension_only`.
4. A dynamic-programming bucker that maximises net log value over fixed
   candidate lengths.
5. A residue ledger with volume, ODT, moisture, chip and hog yield.  Density,
   moisture, chip and hog values are labelled assumptions.

## Files

| File | Content |
|---|---|
| `schema.md` | Field-by-field schema and evidence-tier rules. |
| `tree_list.csv` | Input tree list. |
| `bucked_logs.csv` | One row per recovered log. |
| `residue_ledger.csv` | One row per stem. |
| `reconciliation.csv` | Per-tree and total volume reconciliation. |
| `reconciliation_summary.json` | Machine-readable totals and checks. |
| `taper_registry.csv` | Taper registry used by the run. |
| `grade_rules.csv` | Pilot sort/price rule set used by the run. |
| `manifest.json` | Code, configuration, checksums, counts and scope. |

## What is a pilot vs national

- **Pilot:** the schema wiring, taper dispatch, bucking DP, residue accounting,
  and reconciliation on a small synthetic Quebec tree list.
- **Not national:** the tree list is synthetic and unweighted; the sort set and
  prices are assumptions; there is no provincial inventory expansion, no
  official grade assignment, and no national aggregation.  Do not cite these
  volumes as Quebec or Canada supply.

## Reproduce

```bash
.venv/bin/python -m workflows.national.bucking.national_bucking_pilot   --out-dir data/derived/national/bucking/national_bucking_pilot_v0
```
