# BC OSeCAN residue cap reconciliation

Status: **FRESH-side provisional**.  This note bridges the 2026-11-17 cap
(`bc_national_batch_area_joined.csv` sha256 `e0a51d5aa6b1...`) to
the refined 2026-11-18 all-BC chain (`fd12a1a...`).

## 1. Input-hash bridge

| Item | Pre-refinement / cap | Refined / current |
|---|---|---|
| Joined batch sha256 | `e0a51d5aa6b1ec22b9d27451f229a26bed525ee85641b7ce1766fe1c822e411e` | `fd12a1ace118b951ddf1e82d03c17c4b0e63bf4b288814c09526db371c103e7b` |
| Batch log (m3) | 8,936,253,982.256 | 11,282,585,443.417 |
| Batch residue (ODT) | 722,691,930.985 | 823,762,897.518 |
| BC all-species ratio (ODT/m3) | 0.080871910 | 0.073011891 |
| Area weights sha256 | `a173afb4e323...` | `a1882d5e1d0d...` |

The batch totals rose because the species-alias refinement recovered
10,845,346 ha of formerly `UNMAPPED_BC` area into named species.  The cap did
not see that batch: it was built from the stale `e0a51d5...` file.  The
chain manifest already records the current `fd12a1a...` file, so the cap
predates the refinement.

## 2. Old vs new caps (2028+, PJ/yr)

| Case | Zone | Old | New | Delta | Delta % |
|---|---|---:|---:|---:|---:|
| low | B1 | 2.142167 | 2.103194 | -0.038973 | -1.82% |
| low | B2 | 23.547767 | 19.302895 | -4.244872 | -18.03% |
| low | CAN | 25.689934 | 21.406089 | -4.283845 | -16.68% |
| base | B1 | 3.672286 | 3.605475 | -0.066811 | -1.82% |
| base | B2 | 39.286509 | 32.204471 | -7.082038 | -18.03% |
| base | CAN | 42.958795 | 35.809946 | -7.148849 | -16.64% |
| high | B1 | 4.590357 | 4.506844 | -0.083513 | -1.82% |
| high | B2 | 50.459500 | 41.363347 | -9.096154 | -18.03% |
| high | CAN | 55.049858 | 45.870191 | -9.179667 | -16.68% |

2021 values:

| Case | Zone | Old | New | Delta | Delta % |
|---|---|---:|---:|---:|---:|
| low | B1 | 2.145722 | 2.106679 | -0.039043 | -1.82% |
| low | B2 | 28.047733 | 22.589140 | -5.458593 | -19.46% |
| low | CAN | 30.193455 | 24.695820 | -5.497635 | -18.21% |
| base | B1 | 3.678381 | 3.611450 | -0.066931 | -1.82% |
| base | B2 | 46.794140 | 37.687160 | -9.106980 | -19.46% |
| base | CAN | 50.472521 | 41.298610 | -9.173911 | -18.18% |
| high | B1 | 4.597976 | 4.514313 | -0.083663 | -1.82% |
| high | B2 | 60.102284 | 48.405300 | -11.696984 | -19.46% |
| high | CAN | 64.700261 | 52.919613 | -11.780647 | -18.21% |

The base 2028+ total falls from **42.958795 PJ**
to **35.809946 PJ**.  Low/high cases move proportionally; costs are
unchanged at 2.456978 / 3.194071 / 1.965582 $/GJ.

## 3. Decomposition of the change (2028, base case)

`cap = log volume x taper ratio x recovery x 18.5 / 1e6`.  The three factors
are shown as ratios; the final column is the exact cap change.

| Zone | Old log (m3) | New log (m3) | Log | Old taper (ODT/m3) | New taper (ODT/m3) | Taper | Old recovery | New recovery | Recovery | Cap change |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| B1 | 9,120,804.865 | 9,120,804.865 | -0.00% | 0.036272735 | 0.035612818 | -1.82% | 0.600000000 | 0.600000000 | +0.00% | -1.82% |
| B2 | 34,249,970.935 | 34,249,970.935 | +0.00% | 0.106181718 | 0.087040720 | -18.03% | 0.583931303 | 0.583931303 | +0.00% | -18.03% |

The recovery factor is deliberately **1.000000**: the base recovery is held at
the published 2026-11-17 calibration.  The refined batch reduces the B2 gross
taper ratio from 0.106181 to 0.087041 (-18.03%), which is the dominant driver.
The FFCM-implied recovery on the refined batch is
0.723799
for B2, not 0.583931; re-deriving it would raise the B2 cap to about 39.9 PJ
and would not reconcile with the chain.  It is reported as a diagnostic and an
open evidence question.

## 4. Chain and energy cap agreement

Chain recoverable residue from `bc_supply_by_zone.csv`:

| Year | Zone | Cap (PJ) | Chain recoverable (PJ) | Difference |
|---:|---|---:|---:|---:|
| 2021 | B1 | 3.611450 | 3.611450 | +0.000000% |
| 2021 | B2 | 37.687160 | 37.687160 | -0.000000% |
| 2028 | B1 | 3.605475 | 3.605475 | +0.000000% |
| 2028 | B2 | 32.204471 | 32.204471 | -0.000000% |

The 2028 values agree exactly because the time path now uses the same
matched-cell zone taper ratio as the chain and the same published recovery
fractions.  The zone split of the batch is:

| Zone | Matched log (m3) | Matched residue (ODT) | Ratio (ODT/m3) |
|---|---:|---:|---:|
| B1 | 3,077,735,121.344 | 109,606,819.214 | 0.035612818 |
| B2 | 8,204,850,322.074 | 714,156,078.303 | 0.087040720 |

## 5. Residual disagreement and smallest fix

No cap/chain disagreement remains at the published basis.  The residual issue
is the FFCM-implied recovery diagnostic: on the refined B2 taper the FFCM
roadside stream is 0.723799 of gross taper, versus the published 0.583931.
If the project decides the FFCM-implied basis is authoritative, the smallest
fix is to replace `PUBLISHED_BASE_RECOVERY["B2"]` with the implied value,
rebuild the time path and chain together, and update the manifest; that would
raise the B2 cap to about 39.9 PJ, not lower it to 32.2 PJ.
