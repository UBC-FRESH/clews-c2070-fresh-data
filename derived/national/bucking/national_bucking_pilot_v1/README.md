# National bucking pilot v1 — 13 jurisdictions

**Scope: representative synthetic pilot, not inventory and not a national
supply estimate.**

This directory exercises the national bucking contracts across all 13
jurisdictions using ten representative trees per province.  Species shares use
the open NFI coverage ecodistrict table where available; Alberta, Ontario, Nova
Scotia and Nunavut use explicit documented composition assumptions because the
open coverage table has no provincial rows for them.  DBH draws use NFI
national species p05/p50/p95 quantiles with an 8 cm merchantable lower bound;
height uses the NFI national log-linear height-diameter fit.  The trees are
deterministic synthetic draws.

Taper dispatch:

- Quebec: Schneider (2013) local published fixed-effect taper.
- British Columbia: Kozak (2004) local published Version 6 taper via `nemora`.
- Other provinces: documented donor taper (BC Kozak for western/boreal
  provinces, Quebec Schneider for eastern/Acadian provinces).  Every donor row
  says `taper_status=donor_published`; the BEC anchor is a BC anchor, not a
  local BEC zone.

Products are dimension-only pilot sorts.  `grade=not_assigned`; no official
grade, policy grade, or market price is claimed.  Residue is defined as taper
total minus recovered gross logs, so the stump section above the 0.3 m taper
base, top and unmerchantable material are explicit; volume below the taper base
is outside the ledger.

## Files

| File | Content |
|---|---|
| `tree_list.csv` | Combined representative tree list. |
| `tree_lists/*.csv` | Per-province tree lists. |
| `bucked_logs.csv` | One row per recovered log. |
| `residue_ledger.csv` | One row per stem. |
| `reconciliation.csv` | Per-tree volume reconciliation. |
| `province_summary.csv` | Logs, residue and product shares by province. |
| `coefficient_comparison.csv` | Model ratios versus facility-chain coefficients. |
| `summary.json` | Machine-readable totals, labels and checks. |
| `report.md` | Human-readable pilot report. |
| `manifest.json` | Code, inputs, outputs, checksums and scope. |
| `taper_dispatch.csv` | Taper actually resolved for every tree. |
| `sort_rules.csv` | National dimension-only pilot sort set. |
| `schema.md` | Field and evidence-tier contract. |

## Reproduce

```bash
.venv/bin/python -m workflows.national.bucking.national_bucking_pilot_v1   --out-dir data/derived/national/bucking/national_bucking_pilot_v1
```
