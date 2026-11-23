# Four-province measured bucking pilot v0

Pilot bucking for **BC, QC, NB and YT only**.  The other nine provinces are
deliberately excluded.  All four tree lists are measured; no synthetic trees
are introduced.

| File | Content |
|---|---|
| `tree_list.csv` | Selected measured stems with provenance and expansion |
| `sample_selection.csv` | Per-stratum source count and retained stem audit |
| `sample_audit.csv` | Source, excluded and selected expansion by province |
| `bucked_logs.csv` | Recovered dimension-sorted logs |
| `residue_ledger.csv` | Per-stem residue and chip/hog accounting |
| `province_summary.csv` | Logs, residue and product shares by province |
| `taper_dispatch.csv` | Per-tree taper, local/donor status and proxy flag |
| `taper_coverage.csv` | Taper coverage by province and species |
| `coefficient_comparison.csv` | Model versus facility feedstock coefficients |
| `summary.json`, `report.md`, `manifest.json` | Machine-readable audit and report |

Reproduce:

```bash
.venv/bin/python -m workflows.national.bucking.four_province_bucking_pilot \
  --out-dir data/derived/national/bucking/four_province_bucking_pilot_v0
```
