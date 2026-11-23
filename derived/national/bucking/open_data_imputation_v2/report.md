# E2 v2 open-inventory-informed tree lists

**Status:** E2b open-inventory-informed screening lists; `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`. No request, DUA, restricted data or official OSeCAN change is used.

## Province sources and fields

| Province | Source | Fields used | Inventory informed |
|---|---|---|---|
| AB | AVI Crown (full FGDB) | SP1..SP5, SP1_PER..SP5_PER, HEIGHT, ORIGIN, PHOTO_YR | yes: species, height, age |
| SK | FRI Forest Stands (500-stand open sample) | CSG, HEIGHT, BA, QMD, MSTEMS, GBVOL, GMVOL8 | yes: group, height, QMD, volume |
| MB | FRI 1970s (full FGDB) | SPECIES composition, AGE_YRPHOTO, AREA_HA | yes: species, age; donor H-D |
| NS | Forest Inventory (full DBF) | SP1..SP4, SP1P..SP4P, HEIGHT, AVDI, TOTBA, TOTMRVOL, HECTARES | yes: species, height, AVDI, volume |
| PE | CLUI 2010 + EFI2020 (500-row samples) | COVER/PER, HEIGHT; topht, bamerch, tphmerch, gtv | yes: species, height, inferred QMD, volume |
| ON | no open stand attributes | SCANFI composition + measured donor geometry | no: donor-only |
| NL | land cover only | SCANFI composition + measured donor geometry | no: donor-only |
| NT | ATLAS broad vegetation only | SCANFI composition + measured donor geometry | no: donor-only |
| NU | no territorial inventory | SCANFI composition + measured donor geometry | no: donor-only |

## Inference and labels

- AB: `dbh_basis=inferred_dbh`; `ln(DBH_cm)=a+b ln(H_m-1.3)` is fitted to measured BC/QC/NB/YT donor stems by NFI species or species group and applied to AVI height. AB has no volume field.
- SK: `dbh_basis=inventory_qmd`, `joint_basis=paired_local_marginals`; FRI height and QMD marginals are paired by rank because the stand vector has no tree-level joint distribution. CSG constrains SCANFI species shares.
- MB: `joint_basis=donor_joint`; MB species and age are local, but height and DBH are missing from the open 1970s attributes and therefore use the measured donor joint.
- NS: `joint_basis=local_joint`; species, height, AVDI and TOTMRVOL are carried from the same stand polygon.
- PE: `dbh_basis=inferred_dbh`, `joint_basis=paired_multi_source`; CLUI supplies species/height and EFI supplies `QMD=100*sqrt(bamerch/(tphmerch*pi/4))`, BA and volume. The two sources are paired by rank, not by location.
- ON/NL/NT/NU: `joint_basis=donor_joint`; no open stand species/height/DBH distribution exists, so SCANFI composition and measured donor geometry are used.
- All nine provinces keep 36 representative stems and a 1000 stems/ha expansion.

## E2 v1 to v2 changes

| Province | H v1→v2 (m) | DBH v1→v2 (cm) | Solid v1→v2 | Pulp v1→v2 | Residue ODT/m3 v1→v2 | Species L1 |
|---|---:|---:|---:|---:|---:|---:|
| AB | 12.40→14.50 | 13.16→21.83 | 0.623→0.415 | 0.377→0.585 | 0.1325→0.1598 | 0.607 |
| SK | 12.14→11.31 | 12.43→9.80 | 0.499→0.357 | 0.501→0.643 | 0.1688→0.6349 | 0.442 |
| MB | 11.53→12.13 | 12.15→12.17 | 0.539→0.422 | 0.461→0.578 | 0.2181→0.1940 | 0.394 |
| ON | 11.76→11.92 | 12.37→12.59 | 0.492→0.492 | 0.508→0.508 | 0.2077→0.2102 | 0.000 |
| NS | 13.77→12.23 | 18.79→14.59 | 0.425→0.230 | 0.575→0.770 | 0.1935→0.2965 | 0.714 |
| PE | 14.32→13.04 | 19.15→17.22 | 0.409→0.273 | 0.591→0.727 | 0.1841→0.2380 | 0.758 |
| NL | 12.82→12.87 | 16.85→16.91 | 0.513→0.513 | 0.487→0.487 | 0.2197→0.2202 | 0.000 |
| NT | 11.61→11.92 | 12.32→12.64 | 0.641→0.641 | 0.359→0.359 | 0.1739→0.1770 | 0.000 |
| NU | 11.06→11.24 | 11.83→11.98 | 0.718→0.718 | 0.282→0.282 | 0.2742→0.2770 | 0.000 |

## Checks

| Check | Result |
|---|---|
| nine_provinces | PASS |
| thirty_six_trees_each | PASS |
| expansion_totals_1000 | PASS |
| e2b_provenance | PASS |
| imputed_not_measured | PASS |
| no_national_claim | PASS |
| inventory_informed_flags | PASS |
| distribution_labels_present | PASS |
| ab_dbh_inferred | PASS |
| pe_dbh_inferred | PASS |
| ns_local_joint | PASS |
| sk_paired_marginals | PASS |
| donor_only_provinces_labelled | PASS |
| numeric_tree_not_nan | PASS |
| numeric_tree_non_negative | PASS |
| numeric_summary_not_nan | PASS |
| summary_non_negative | PASS |
| volume_balance | PASS |
| residue_balance | PASS |
| coefficient_scenarios | PASS |
| comparison_nine_rows | PASS |
| comparison_numeric | PASS |
| no_dua_dependency | PASS |
| no_official_osecan_change | PASS |

## Limits

- E2 v2 is not E1 measurement. Local inventory attributes are stand-level photo-interpretation or LiDAR model output, not measured tree lists.
- ON, NL, NT and NU remain donor-only because their open layers lack the stand attributes needed for a distribution.
- SK and PE inputs are checked-in 500-row samples, not the full open layers; the full layers are REST services and are not redistributed.
- Taper geometry remains a published cross-jurisdiction donor (BC Kozak or QC Schneider). No local provincial taper is claimed.
- No national supply or official grade claim is made.
