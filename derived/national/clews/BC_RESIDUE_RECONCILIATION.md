# BC OSeCAN residue cap reconciliation

Status: **FRESH-side provisional; basis resolved 2026-11-18**.  This note
bridges the 2026-11-17 cap (`bc_national_batch_area_joined.csv` sha256
`e0a51d5aa6b1...`) through the interim held-calibration cap to the
adopted FFCM-implied basis on the refined 2026-11-18 all-BC chain
(`fd12a1a...`).

## 1. Input-hash bridge

| Item | Pre-refinement / cap | Refined / current |
|---|---|---|
| Joined batch sha256 | `e0a51d5aa6b1ec22b9d27451f229a26bed525ee85641b7ce1766fe1c822e411e` | `fd12a1ace118b951ddf1e82d03c17c4b0e63bf4b288814c09526db371c103e7b` |
| Batch log (m3) | 8,936,253,982.256 | 11,282,585,443.417 |
| Batch residue (ODT) | 722,691,930.985 | 823,762,897.518 |
| BC all-species ratio (ODT/m3) | 0.080871910 | 0.073011891 |
| Area weights sha256 | `a173afb4e323...` | `a1882d5e1d0d...` |

The batch totals rose because the species-alias refinement recovered
10,845,346 ha of formerly `UNMAPPED_BC` area into named species.

## 2. Basis decision

The refined batch changed the B2 gross taper ratio from 0.106181 to
0.087041 ODT/m3, so the FFCM-implied B2 recovery is now recomputed from the
current batch and FFCM ledger:

`implied_B2 = ffcm_residue_B2 / (ffcm_log_B2 x taper_ratio_B2)`

= 7,011,925.584 / (111,300,406.101 x
0.087040720) =
**0.723799161**.

This is the adopted base (asserted at build time to 0.723799
within 1e-05 and to [0.2, 1.0]).  B1 stays at the
documented **0.600000** fallback because its implied
1.769026 is out of bounds.

| Basis | B1 2028+ (PJ) | B2 2028+ (PJ) | Total 2028+ (PJ) |
|---|---:|---:|---:|
| Old published 2026-11-17 | 3.672286 | 39.286509 | 42.958795 |
| Interim held calibration | 3.605475 | 32.204471 | 35.809946 |
| Adopted FFCM-implied | 3.605475 | 39.918341 | 43.523816 |

The old published 42.958795 PJ held B2 at 0.583931, a calibration tied to the
pre-refinement taper.  The interim 35.809946 PJ deliberately held that stale
calibration and is superseded.  The adopted total is
**43.523816 PJ**.

## 3. Old published vs adopted caps (2028+, PJ/yr)

| Case | Zone | Old | Adopted | Delta | Delta % |
|---|---|---:|---:|---:|---:|
| low | B1 | 2.142167 | 2.103194 | -0.038973 | -1.82% |
| low | B2 | 23.547767 | 19.302895 | -4.244872 | -18.03% |
| low | CAN | 25.689934 | 21.406089 | -4.283845 | -16.68% |
| base | B1 | 3.672286 | 3.605475 | -0.066811 | -1.82% |
| base | B2 | 39.286509 | 39.918341 | +0.631832 | +1.61% |
| base | CAN | 42.958795 | 43.523816 | +0.565021 | +1.32% |
| high | B1 | 4.590357 | 4.506844 | -0.083513 | -1.82% |
| high | B2 | 50.459500 | 41.363347 | -9.096154 | -18.03% |
| high | CAN | 55.049858 | 45.870191 | -9.179667 | -16.68% |

2021 values:

| Case | Zone | Old | Adopted | Delta | Delta % |
|---|---|---:|---:|---:|---:|
| low | B1 | 2.145722 | 2.106679 | -0.039043 | -1.82% |
| low | B2 | 28.047733 | 22.589140 | -5.458593 | -19.46% |
| low | CAN | 30.193455 | 24.695820 | -5.497635 | -18.21% |
| base | B1 | 3.678381 | 3.611450 | -0.066931 | -1.82% |
| base | B2 | 46.794140 | 46.714288 | -0.079853 | -0.17% |
| base | CAN | 50.472521 | 50.325738 | -0.146783 | -0.29% |
| high | B1 | 4.597976 | 4.514313 | -0.083663 | -1.82% |
| high | B2 | 60.102284 | 48.405300 | -11.696984 | -19.46% |
| high | CAN | 64.700261 | 52.919613 | -11.780647 | -18.21% |

Costs are unchanged at 2.456978 / 3.194071 / 1.965582 $/GJ.

## 4. Decomposition vs the old published basis (2028, base case)

`cap = log volume x taper ratio x recovery x 18.5 / 1e6`.

| Zone | Old log (m3) | New log (m3) | Log | Old taper (ODT/m3) | New taper (ODT/m3) | Taper | Old recovery | New recovery | Recovery | Cap change |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| B1 | 9,120,804.865 | 9,120,804.865 | -0.00% | 0.036272735 | 0.035612818 | -1.82% | 0.600000000 | 0.600000000 | +0.00% | -1.82% |
| B2 | 34,249,970.935 | 34,249,970.935 | +0.00% | 0.106181718 | 0.087040720 | -18.03% | 0.583931303 | 0.723799161 | +23.95% | +1.61% |

For B2 the taper refinement (-18.03%) is more than offset by adopting the
FFCM-implied recovery (0.583931 -> 0.723799,
+23.95%), so the cap rises +1.61% versus the old published value.
B1 is unchanged in recovery and moves only with the zone taper.

## 5. Chain and energy cap agreement

Chain recoverable residue from `bc_supply_by_zone.csv`:

| Year | Zone | Cap (PJ) | Chain recoverable (PJ) | Difference |
|---:|---|---:|---:|---:|
| 2021 | B1 | 3.611450 | 3.611450 | +0.000000% |
| 2021 | B2 | 46.714288 | 46.714288 | -0.000000% |
| 2028 | B1 | 3.605475 | 3.605475 | +0.000000% |
| 2028 | B2 | 39.918341 | 39.918341 | -0.000000% |

The time path and the chain share the same matched-cell zone taper ratio and
the same base recovery fraction, so the cap and chain recoverable residue agree
per zone.  The zone split of the batch is:

| Zone | Matched log (m3) | Matched residue (ODT) | Ratio (ODT/m3) |
|---|---:|---:|---:|
| B1 | 3,077,735,121.344 | 109,606,819.214 | 0.035612818 |
| B2 | 8,204,850,322.074 | 714,156,078.303 | 0.087040720 |

## 6. Validation

- B2 implied recovery is recomputed and asserted at
  0.723799161 (expected
  0.723799, tolerance 1e-05).
- B1 uses the documented 0.60 fallback; its implied value is out of bounds.
- Cases remain monotonic: low 0.35 < base < high 0.75.
- Cap equals chain recoverable residue per zone within 1% after the chain
  rebuild; the test suite re-checks the 2028 rows.
- `SUPBCW` is the exact B1+B2 rollup and remains comparison-only.
