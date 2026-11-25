# Harvest residue component breakdown v1 (119 Mm³)

## 1. Scope

This provenance artifact splits the committed 119 Mm³ gross harvest
residue into stem, branch and foliage components. It adds no new
supply, recovery, siting, cost or policy result. Every row is a
`model_estimate`; `observed=false`; `policy_grade=false`;
`national_claim=false`; `official_osecan_changed=false`;
`ui_changed=false`.

Inputs:

- `data/derived/national/facilities/national_product_chain_v5/product_chain_by_province.csv`
- `data/derived/national/bucking/four_province_bucking_pilot_v0/province_summary.csv`
- `data/derived/national/bucking/open_data_imputation_v3/province_summary.csv`
- `docs/model-card-national-facility-chain.md` §5.3

## 2. Method

For province `p`, with chain stem ODT `S_p`, chain branch+foliage
ODT `B_p`, chain total ODT `T_p`, and source ratio
`r_p = branch_odt_expanded / (branch_odt_expanded +
foliage_odt_expanded)`:

```
branch_odt_p  = B_p * r_p
foliage_odt_p = B_p - branch_odt_p
stem_pj_p     = S_p * 18.5 / 1e6
branch_pj_p   = branch_odt_p * 18.5 / 1e6
foliage_pj_p  = foliage_odt_p * 18.5 / 1e6
total_pj_p    = T_p * 18.5 / 1e6
recoverable_pj(f) = f * total_pj_p
```

E1 measured ratios apply to BC, QC, NB and YT. E2c open-data
imputation ratios apply to AB, SK, MB, ON, NS, PE, NL and NT. NU has
zero modelled harvest.

Tops are not separately modelled. Stem residue is the taper total
from a 0.3 m stump to the tree tip minus recovered logs, so it
already includes stump, top and unmerchantable sections. No tops
number is invented.

## 3. National totals

| Component | ODT | PJ | Share of gross |
|---|---:|---:|---:|
| Stem | 6,909,832.991 | 127.832 | 28.76% |
| Branch | 11,669,976.957 | 215.895 | 48.58% |
| Foliage | 5,442,393.623 | 100.684 | 22.66% |
| **Total** | **24,022,203.572** | **444.411** | **100.00%** |
| Branch+foliage | 17,112,370.580 | 316.579 | 71.24% |

Gross harvest residue is **444.411 PJ**
(444.410766 PJ unrounded); the display value is
**444.411 PJ**. Branch+foliage is
**316.579 PJ**.

Uniform recovery scenarios applied to gross total residue:

| Factor | Recoverable PJ |
|---:|---:|
| 0.35 | **155.544** |
| 0.60 | **266.646** |
| 0.75 | **333.308** |

The recovery denominator is gross total residue
(444.411 PJ;
24,022,203.572 ODT).

0.35/0.60/0.75 are uniform arithmetic scenarios applied to gross total residue. No environmental, operational, technical, economic or accessibility recovery constraint is modelled; 0.60 is a reference scenario, not a calibrated recovery factor.

## 4. Provincial breakdown

| Province | Tier | Stem PJ | Branch PJ | Foliage PJ | Total PJ | Branch+foliage PJ |
|---|---|---:|---:|---:|---:|---:|
| BC | measured_bucking_pilot | 30.011 | 56.630 | 32.895 | 119.536 | 89.525 |
| AB | E2c_open_inventory_density_calibrated | 6.164 | 49.563 | 11.932 | 67.659 | 61.495 |
| SK | E2c_open_inventory_density_calibrated | 28.123 | 16.254 | 6.653 | 51.031 | 22.908 |
| MB | E2c_open_inventory_density_calibrated | 1.778 | 1.494 | 0.802 | 4.074 | 2.295 |
| ON | E2c_open_inventory_density_calibrated | 21.210 | 21.121 | 10.137 | 52.469 | 31.258 |
| QC | measured_bucking_pilot | 29.317 | 50.408 | 27.609 | 107.334 | 78.017 |
| NB | measured_bucking_pilot | 3.500 | 12.585 | 5.533 | 21.618 | 18.118 |
| NS | E2c_open_inventory_density_calibrated | 5.444 | 4.493 | 3.161 | 13.098 | 7.654 |
| PE | E2c_open_inventory_density_calibrated | 0.362 | 0.605 | 0.363 | 1.330 | 0.969 |
| NL | E2c_open_inventory_density_calibrated | 1.773 | 2.626 | 1.523 | 5.923 | 4.149 |
| YT | measured_bucking_pilot | 0.100 | 0.068 | 0.051 | 0.219 | 0.119 |
| NT | E2c_open_inventory_density_calibrated | 0.049 | 0.046 | 0.024 | 0.119 | 0.070 |
| NU | E2c_open_inventory_density_calibrated | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

The full ODT, PJ, share and source-ratio fields are in
`component_by_province.csv`.

## 5. Validation

| Check | Status |
|---|---|
| `row_count_13` | PASS |
| `province_set_matches_chain` | PASS |
| `tier_mapping_matches` | PASS |
| `component_conservation_all_provinces` | PASS |
| `national_total_matches_expected` | PASS |
| `national_branch_foliage_matches_expected` | PASS |
| `national_recoverable_060_matches_expected` | PASS |
| `model_card_5_3_cross_check` | PASS |
| `shares_sum_to_one` | PASS |
| `labels_complete` | PASS |

Per-province stem + branch + foliage equals the chain total
within
1.00e-05 ODT.
The national total is
444.410766 PJ.
The maximum absolute province delta against model-card §5.3 is
0.000472 PJ at a
0.001 PJ tolerance.

## 6. Caveats and non-claims

- E2c ratios come from 36-tree synthetic open-data imputation
  lists, not measured provincial components. E1 ratios are
  measured-tree-list values, but branch and foliage dry mass is
  computed from published CFS equations rather than weighed.
- The branch/foliage split is a ratio transfer from the source
  province summary. It is not a new inventory or allometric
  estimate.
- Tops are not separately modelled and no tops number is
  reported. Stem residue includes stump, top and unmerchantable
  sections by construction.
- No environmental, operational, technical, economic or
  accessibility recovery constraint is modelled. The
  0.35/0.60/0.75 values are uniform arithmetic scenarios, and
  0.60 is not calibrated.
- No facility, transport, cost, landbase, tenure, legal, policy
  or national supply claim is made.
- No UI change and no official OSeCAN change is made.

## 7. Reproduce

```bash
.venv/bin/python -m workflows.national.facilities.harvest_residue_component_breakdown_v1
.venv/bin/pytest -q tests/test_harvest_residue_component_breakdown_v1.py
```

Input SHA-256:

| Input | SHA-256 |
|---|---|
| `data/derived/national/bucking/four_province_bucking_pilot_v0/province_summary.csv` | `d1327a70d73a5031438d1633943e1da6718b5509c88c457f51ff47c6bd99c8fc` |
| `data/derived/national/bucking/open_data_imputation_v3/province_summary.csv` | `d3ffd49e3c9e436acc6db9a6f50bd25833318134ceb3f7ae70b57eb82886d17d` |
| `data/derived/national/facilities/national_product_chain_v5/product_chain_by_province.csv` | `879e523ebf52d75508c9c9ee0e88a923bdf8d37ad70e2039b7c0991280330184` |
| `docs/model-card-national-facility-chain.md` | `bbfcf07dc8b436dc878384dfd548cfeec747d9d694f9a2f511c2d1b135da1032` |

