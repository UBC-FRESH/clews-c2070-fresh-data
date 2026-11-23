# National bucking pilot v2 — measured BC list

**Scope: pilot.  BC tree geometry is measured FAIB PSP TSA24 data; the other 12
jurisdictions keep the v1 representative synthetic lists.  Not inventory, not a
national supply estimate, not an official grade.**

BC replaces the ten v1 synthetic trees with a post-stratified aggregate of
measured TSA24 PSP stems.  Within each species x BEC zone x 2.5 cm DBH stratum,
one PHF-weighted median stem is retained and assigned the stratum's summed
`PHF_TREE` expansion factor.  The BC list preserves the source expansion total
exactly and retains the measured DBH/height pair.  See
`bc_tree_list_selection.csv`.

BC is bucked twice:

1. `bc_tipsy_*`: BC Kozak (2004) taper with the BC interior TIPSY 4.5 dimension
   sorts, matching the `bc_psp_validation_v0` rule set.
2. `bucked_logs.csv` / `residue_ledger.csv`: the national pilot dimension sort
   set, so v1 and v2 national product shares are comparable.

The other 12 jurisdictions use the v1 local/donor taper dispatch and national
pilot sorts.  `grade=not_assigned`; no official grade, policy grade, or market
price is claimed.  Residue is taper total minus recovered gross logs per stem.

## Files

| File | Content |
|---|---|
| `bc_tree_list_selection.csv` | BC stratum selection and source provenance |
| `tree_lists/BC.csv` | BC measured aggregate tree list |
| `bc_tipsy_logs.csv`, `bc_tipsy_residue.csv` | BC TIPSY dimension-sort rerun |
| `bc_tipsy_sort_rules.yaml`, `bc_tipsy_sort_rules.csv` | Exact BC TIPSY rule file used |
| `bucked_logs.csv`, `residue_ledger.csv` | National-sort pilot |
| `province_summary.csv` | Per-province unweighted and expanded metrics |
| `coefficient_comparison.csv` | 13-province facility screening |
| `bc_facility_comparison.csv` | BC v1/v2 variant fit to facility coefficients |
| `v1_v2_comparison.csv` | Province and national v1-to-v2 deltas |
| `bc_population_reconciliation.csv` | v2 list versus full v0 population |
| `summary.json`, `report.md`, `manifest.json` | Machine-readable and human-readable audit |

## Reproduce

```bash
.venv/bin/python -m workflows.national.bucking.national_bucking_pilot_v2 \
  --out-dir data/derived/national/bucking/national_bucking_pilot_v2
```
