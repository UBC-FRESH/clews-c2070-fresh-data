# RSYC National Volume Benchmark Report

**Date:** 2026-11-18  
**Scope:** Benchmark the RSYC national **volume** curves against BC FAIB PSP
observations, the Quebec BFEC 5-unit AAC sample, and the Lochhead MGM
western-boreal yield curves. No above-ground biomass (AGB) benchmark was run.  
**Status:** Exploratory volume-only benchmark. Outputs written, not committed.
All correction factors are withheld as candidates; none is released for use.

## 1. Bottom line

RSYC is a plausible **volume-only** national backbone at the scale of regional
means. It is not a validated AGB product and not a complete national yield-curve
model. The benchmark does not test AGB, height, taper, or grade, so no AGB claim
is made here.

At the scale tested:

- RSYC reproduces several interior BC and QC regional means within about ±15%
  (BC Boreal Foothills −1.2%, Columbia Montane Cordillera +1.2%, Central
  Montane Cordillera +7.0%, Southern Montane Cordillera +7.1%; QC age-50 total
  −6.7%).
- It strongly underpredicted coastal BC and old stands, and overpredicted
  several young western-boreal MGM strata.
- Its curve shape remains a national species shape rescaled by ecoprovince; it
  cannot reproduce local old-growth trajectories or local MAI behaviour.
- The MGM equation is now **verified** against the pinned upstream loader, but
  the MGM comparison remains a province-level screen without an FMU key.
- No correction factor is defensible yet. `local_correction_factors.csv` is a
  candidate-only table with `status = withheld`; the holdout protocol has been
  evaluated but does not justify release.

## 2. Review fixes applied in this revision

### 2.1 MGM equation verified, cohort problem fixed, MAI relabelled

The previous benchmark used an inferred power–exponential form. The exact
upstream expression was fetched and verified:

| Item | Verified value |
|---|---|
| Repository | `UBC-FRESH/spades_ws3` |
| Commit | `1847872` (`184787233aaa761f7b3eda54155d9dbbe50bf779`, 2022-03-30) |
| File | `python/spadesws3.py` |
| Function | `bootstrap_yields.f` |
| Expression | `a * pow(x, b) * math.exp(-c * x)` |
| Age origin | 0 years |
| Age units | years |
| Native support | 0–350 years, sampled every 10 years |
| Total volume | `cvol + dvol` via `_SUM` |
| Fetched file SHA-256 | `2b591065c25869a48d4a396edfb2502e78013ae44228abcb6847a2ecd3eea590` |

The working copy of the fetched source is `tmp/rsyc_review/spadesws3_1847872.py`
(not committed). The benchmark now uses exactly
`c_a*Age^c_b*exp(-c_c*Age) + d_a*Age^d_b*exp(-d_c*Age)`.

The cohort filter was removed. The old code required
`Age == age_encoded_in_ygrp`, which selected only the starting row of each
yield group and changed the cohort at every target age. The benchmark now
evaluates each fixed yield group at every requested age inside its stored
31-year window. Starting age is retained as `starting_age`,
`starting_age_stratum`, and `age_offset`; the summary is explicitly a set of
starting-age strata, not a longitudinal trajectory.

MGM MAI is now computed over the native 0–350-year support and reported as an
**endpoint maximum**, not a culmination. Maxima at 350 are right-censored
(`mgm_mai_status = right_censored_at_native_max`). RSYC remains truncated at its
operational 150-year limit. In this sample only 0.5% of MGM group maxima are
right-censored at 350; the rest are interior maxima over the native support.

### 2.2 QC zero-total and mix fabrication removed

The previous code assigned a 50/50 conifer/deciduous mix whenever observed
total volume was zero. That fabricated a prediction for zero-yield tables (for
example unit 3152, `tbl_dde1384a6d55`, received 162.77 m³/ha at age 50).

The benchmark now:

- validates that component and total volumes are finite and non-negative;
- validates mass balance (`conifer + deciduous == total`, relative/absolute
  tolerance `1e-6`);
- emits a total-volume prediction only for positive, balanced totals;
- puts zero-total rows in a separate stratum
  (`rsyc_vs_qc_zero_total.csv`) and never assigns them a mix;
- writes any invalid/mismatched rows to `rsyc_vs_qc_invalid_mix.csv`;
- computes hit rates only on positive observed values and publishes the
  denominator (`n_positive_observed`) in the CSV and JSON outputs.

At the three target ages there are 693 productive curve-age rows: 690 positive
totals, 3 zero totals (one table at ages 50/100/150), 0 invalid/mismatched
rows. The total-volume metrics therefore use n = 230 curves at each age, not
231.

### 2.3 BC fallback geography and composite BA accounting fixed

The previous code kept `ecoprovince = null` for BEC-fallback visits, collapsing
them into a blank region, and sliced BEC labels to three characters, which
turned `CHxw`/`MHmm1` into `CHx`/`MHm`. It also renormalised the composite over
resolved species while reporting the code-mapped BA share, so the reported BA
was not the BA actually used.

The benchmark now:

- parses BEC labels with an explicit zone vocabulary, longest zone first, and
  retains zone and subzone (`CWHvm1 → CWH/vm`, `CHxw → CH/xw`,
  `MHmm1 → MH/mm`, `SBPSmc → SBPS/mc`); unknown labels such as `CMAunp` remain
  unresolved rather than being sliced;
- resolves the fallback to a real, validated ecoprovince stratum and records
  the match basis (`tsa_dominant_vri` vs `bec_zone_fallback`);
- groups all BC metrics by ecoprovince and match basis, so fallback visits
  cannot be mistaken for TSA-dominant assignments;
- reports total BA, code-mapped BA, curve-resolved BA, species-resolved BA,
  group-resolved BA, code-unmapped BA, and curve-unresolved BA separately;
- keeps code-unmapped and curve-unresolved BA in the denominator of the primary
  composite (`predicted_composite`). A second, curve-resolved-only composite
  (`predicted_composite_curve_ba`) is reported for transparency but is not the
  primary comparison.

All 1,544 matched fallback visits now have a non-null ecoprovince. In this
sample the fallback visits are CWH (coarse default: Pacific Maritime/Southern
Coastal Mountains) and are grouped separately under `bec_zone_fallback`. Five
additional fallback attempts (ICH/IDF) had no RSYC curve and were dropped; they
are counted in `skip_counts.no_curve`.

BA accounting across the 19,536 matched visits:

| BA category | Sum (m²/ha across visits) | Share |
|---|---:|---:|
| Total live BA | 935,457.8 | 100.0% |
| Code-mapped BA | 914,494.2 | 97.8% |
| Curve-resolved BA | 914,494.2 | 97.8% |
| Species-resolved BA | 914,494.2 | 97.8% |
| Group-resolved BA | 0.0 | 0.0% |
| Code-unmapped BA (kept in denominator) | 20,963.6 | 2.2% |
| Curve-unresolved BA | 0.0 | 0.0% |

6,727 visits contain some code-unmapped BA; 0 visits contain curve-unresolved
BA. The median code-mapped and curve-resolved shares are both 1.0, which is why
the previous median masked the 2.2% aggregate unknown-BA share.

### 2.4 AGB claim narrowed

The benchmark tests volume only. The report no longer calls RSYC an
age-100 volume/AGB backbone. AGB remains an untested RSYC attribute in this
work.

### 2.5 Holdout protocol implemented and evaluated

The planning protocol (`planning/national-rsyc-backbone.md` §5.2) requires
whole-unit holdouts before correction factors are applied. A leave-one-unit-out
level-multiplier evaluation is now implemented:

- **BC:** leave-one-TSA-out, within ecoprovince × leading-species strata.
- **QC:** leave-one-unit-out, within component strata.
- **MGM:** not evaluable because the pinned CSVs contain no FMU/polygon key.

Results are in `benchmark_summary.json` under `holdout`. They are a proxy, not a
predeclared fixed split. All candidate multipliers in
`local_correction_factors.csv` carry `status = withheld` and
`release_decision = not_released_pending_predeclared_holdout`. No correction
factor is released by this revision.

## 3. Method

### 3.1 RSYC prediction

For each ecoprovince × species cell the benchmark uses the exact
`rsyc_volume_model_id` recorded by the national fit. If absent, the lookup falls
back in fixed order: species model → coniferous/broadleaf group model → generic
model. No parameters are averaged or borrowed across ecoprovinces.

Published volume equation:
`V(age) = b1 · exp(−b4 · age) · (1 − exp(−b2 · age))^b3`.

### 3.2 BC FAIB

24,962 PSP visits; 23,440 with non-null source volume; 19,542 remain after
volume > 0 and age 20–150. 19,536 match an RSYC curve. Species composition comes
from the harmonised v0 tree list (expanded live-tree basal area). Metrics compare
both the leading mapped species and the BA-weighted composite; the composite is
the primary stand-level comparison. Ecoprovince is assigned from the dominant
VRI area of the visit's TSA (17,992 visits); TSAs absent from the VRI area table
use the validated BEC-zone fallback (1,544 matched visits). Age bins are 40–60,
80–100, and 120–140 years; metrics use exact visit age.

### 3.3 QC BFEC

5 units (`02651`, `03151`, `03152`, `03451`, `03551`), 32,074 inventory
development types, 236 yield tables, 9,676 curve rows. Productive development
types (`in_model = 1`, `productive = 1`, area > 0) leave 231 curves and 693
curve-age rows at ages 50/100/150. Unit → administrative region → RSYC
ecoprovince is mapped from the sample report (`R03`, `R04`, `R12`); no unit
geometry is available. BFEC total volume is compared with a same-mix RSYC
composite using only validated positive observed totals. Component rows are
reported but flagged **not like-for-like**.

### 3.4 MGM

Four pinned CSVs (`ab_gy.csv`, `bc_gy.csv`, `mb_gy.csv`, `sk_gy.csv`),
951,483 rows total. `VPH` is empty and was not used. Yield groups are parsed
from `ygrp` (`DC-Sb_8_A_80_20` → type `DC`, species `Sb`, height 8, density
`A`, starting age 80, crown closure 20). Only four species are mapped:
`Sb`→`PICE.MAR`, `Sw`→`PICE.GLA`, `Pj`→`PINU.BAN`, `Aw`→`POPU.TRE`.

No spatial key exists, so RSYC is evaluated at **province level** using
area-weighted ecoprovince weights from
`national_area_weights_ecodistrict.csv`. For `POPU.TRE`, which has no species
area weights in the boreal provinces, broadleaf group area weights are used.
The MGM result is a province-level screen, not a stand-level or FMU-level
validation.

## 4. Results

### 4.1 BC FAIB (n = 19,536 matched visits)

**Overall composite (all ages, exact age):**

| n | Observed (m³/ha) | RSYC (m³/ha) | Bias | Rel. RMSE | r | Within ±20% | Within ±30% |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 19,536 | 430 | 290 | −32.4% | 82.6% | 0.59 | 18.7% | 28.8% |

**By ecoprovince, all species, all ages (n ≥ 30):**

| Ecoprovince | Match basis | n | Observed | RSYC | Bias | Rel. RMSE | r | Within ±20% |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Boreal Foothills | TSA-dominant | 215 | 207 | 205 | −1.2% | 47.5% | 0.52 | 32.6% |
| Central Montane Cordillera | TSA-dominant | 1,960 | 196 | 210 | +7.0% | 75.8% | 0.08 | 18.9% |
| Columbia Montane Cordillera | TSA-dominant | 2,947 | 297 | 300 | +1.2% | 60.9% | 0.20 | 24.4% |
| Hay-Slave Lowlands | TSA-dominant | 337 | 254 | 141 | −44.4% | 74.7% | 0.65 | 11.0% |
| Northern Montane Cordillera | TSA-dominant | 2,196 | 222 | 190 | −14.5% | 55.9% | 0.51 | 24.2% |
| Southern Coastal Mountains | BEC fallback | 1,544 | 887 | 384 | −56.7% | 76.7% | 0.63 | 6.0% |
| Southern Coastal Mountains | TSA-dominant | 6,596 | 629 | 333 | −47.0% | 74.5% | 0.60 | 14.6% |
| Southern Montane Cordillera | TSA-dominant | 3,720 | 270 | 289 | +7.1% | 65.3% | 0.09 | 23.4% |

The fallback stratum is now visible and separate; it does not disappear into a
blank region. The CWH fallback default is coarse and can mix north- and
south-coast stands, so the fallback row should not be read as a clean
ecoprovince estimate.

**By age bin (all ecoprovinces and match bases, composite):**

| Age bin | n | Observed | RSYC | Bias | Rel. RMSE | r | Within ±20% |
|---|---:|---:|---:|---:|---:|---:|---:|
| 40–60 | 3,780 | 313 | 261 | −16.4% | 73.8% | 0.66 | 20.7% |
| 80–100 | 4,666 | 478 | 304 | −36.3% | 78.4% | 0.55 | 19.3% |
| 120–140 | 1,567 | 591 | 321 | −45.6% | 85.8% | 0.53 | 15.1% |

Bias grows with age, consistent with a level-plus-shape problem, not a single
level offset. The composite now includes unknown BA in the denominator, so the
all-age bias is more negative than the previous renormalised-only calculation
(−32.4% versus −30.6%).

**By leading species (n ≥ 100, composite, all ages):**

| Species | n | Observed | RSYC | Bias | Rel. RMSE | r | Within ±20% |
|---|---:|---:|---:|---:|---:|---:|---:|
| PSEU.MEN | 5,807 | 394 | 307 | −22.1% | 83.0% | 0.34 | 20.0% |
| PINU.CON | 3,823 | 225 | 203 | −9.8% | 59.3% | 0.35 | 26.1% |
| TSUG.HET | 3,734 | 714 | 373 | −47.8% | 70.7% | 0.64 | 13.1% |
| PICE.GLA | 1,286 | 324 | 233 | −28.1% | 53.9% | 0.56 | 22.9% |
| THUJ.PLI | 999 | 489 | 293 | −40.0% | 84.7% | 0.53 | 12.4% |
| POPU.TRE | 834 | 210 | 186 | −11.4% | 70.3% | 0.35 | 19.1% |
| PICE.SIT | 766 | 1,034 | 414 | −59.9% | 73.6% | 0.73 | 5.4% |
| ABIE.LAS | 655 | 215 | 238 | +11.0% | 60.5% | 0.36 | 24.9% |
| LARI.OCC | 542 | 244 | 395 | +62.1% | 81.2% | 0.18 | 17.7% |
| ABIE.AMA | 431 | 576 | 337 | −41.6% | 79.7% | 0.79 | 9.3% |
| ALNU.RUB | 229 | 384 | 211 | −45.2% | 60.6% | 0.65 | 10.5% |
| PICE.ENG | 155 | 316 | 291 | −7.9% | 57.7% | 0.28 | 20.0% |

### 4.2 QC BFEC (230 positive total curves at each age)

**Pooled same-mix total volume:**

| Age | n curves | Positive denominator | Observed | RSYC | Bias | Rel. RMSE | r | Within ±20% | Within ±30% | Flat curves |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 50 | 230 | 230 | 171 | 160 | −6.7% | 41.7% | 0.35 | 37.0% | 58.3% | 67% |
| 100 | 230 | 230 | 171 | 194 | +13.4% | 42.9% | 0.35 | 37.0% | 49.1% | 100% |
| 150 | 230 | 230 | 171 | 195 | +13.9% | 43.1% | 0.36 | 37.4% | 49.1% | 100% |

**Age-50 total by unit:**

| Unit | Region | n curves | Observed | RSYC | Bias | Rel. RMSE | Within ±20% | Flat at age 50 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| 02651 | R04 | 19 | 77 | 138 | +78.0% | 86.3% | 5.3% | 74% |
| 03151 | R03 | 71 | 156 | 165 | +5.7% | 26.6% | 67.6% | 69% |
| 03152 | R03 | 55 | 135 | 159 | +17.9% | 39.9% | 21.8% | 71% |
| 03451 | R12 | 15 | 258 | 163 | −36.9% | 44.5% | 6.7% | 47% |
| 03551 | R12 | 70 | 222 | 160 | −27.8% | 41.9% | 32.9% | 63% |

The zero-total table (unit 3152, `tbl_dde1384a6d55`, ages 50/100/150) is
excluded from these totals and listed in `rsyc_vs_qc_zero_total.csv`. The
previous +162.77 m³/ha fabricated age-50 prediction for that table no longer
exists.

Component rows (conifer, deciduous) remain **not like-for-like** and are not
used for validation. At age 50 the component comparison is conifer 88.7
observed versus 144.2 RSYC (+62.5%) and deciduous 81.7 versus 178.6 (+118.5%),
but these compare a mixed-stand component with a pure-species potential.

### 4.3 MGM western boreal (47 volume rows, 16 MAI endpoint rows)

The equation is verified, but MGM remains a province-level screen: the pinned
CSVs have no polygon/FMU key, so RSYC is area-weighted across all ecoprovinces
in each province, including non-boreal parts. The volume rows evaluate fixed
yield groups at ages 50/100/150 inside their stored windows; the starting-age
range is reported, and the rows are **starting-age strata**, not a longitudinal
comparison of the same groups across ages.

**Median volume bias by species and age (across province rows):**

| Species | Age | n yield groups | Starting-age range | MGM median (m³/ha) | RSYC (m³/ha) | Median bias | Median rel. RMSE | Mean within ±20% |
|---|---:|---:|---|---:|---:|---:|---:|---:|
| PICE.GLA (Sw) | 50 | 1,555 | 20–50 | 55 | 138 | +95.4% | 120.8% | 9.4% |
| PICE.GLA (Sw) | 100 | 2,200 | 70–100 | 114 | 170 | +60.7% | 84.0% | 15.1% |
| PICE.GLA (Sw) | 150 | 1,834 | 120–150 | 118 | 175 | +53.1% | 80.1% | 16.7% |
| PICE.MAR (Sb) | 50 | 1,770 | 20–50 | 25 | 76 | +188.3% | 200.7% | 4.2% |
| PICE.MAR (Sb) | 100 | 2,784 | 70–100 | 81 | 104 | +41.1% | 67.2% | 25.7% |
| PICE.MAR (Sb) | 150 | 2,297 | 120–150 | 87 | 114 | +39.8% | 68.5% | 24.9% |
| PINU.BAN (Pj) | 50 | 2,114 | 20–50 | 45 | 64 | +15.4% | 74.9% | 11.4% |
| PINU.BAN (Pj) | 100 | 2,135 | 70–100 | 98 | 83 | −17.2% | 63.0% | 22.9% |
| PINU.BAN (Pj) | 150 | 1,406 | 120–150 | 102 | 89 | −37.0% | 76.8% | 16.1% |
| POPU.TRE (Aw) | 50 | 882 | 20–50 | 66 | 143 | +165.7% | 170.4% | 0.0% |
| POPU.TRE (Aw) | 100 | 395 | 70–100 | 108 | 173 | +75.5% | 85.0% | 7.5% |
| POPU.TRE (Aw) | 150 | 32 | 120–150 | 80 | 179 | +154.0% | 163.4% | 0.0% |

`n yield groups` counts MGM yield groups, not independent stands. A single
yield group contributes one row at each age inside its 31-year window; the
starting-age range differs by target age, which is why these are explicitly
starting-age strata.

**MAI endpoint maximum (native 0–350-year support):**

| Species | MGM median endpoint age (province range) | RSYC MAI age | Difference | Right-censored at 350 |
|---|---:|---:|---:|---:|
| PICE.GLA (Sw) | 152.5 (144–162) | 24–27 | −117 to −138 | 0.0% |
| PICE.MAR (Sb) | 117.5 (109–119) | 27–28 | −82 to −91 | 0.8–1.8% in three provinces |
| PINU.BAN (Pj) | 109 (99–117) | 22–28 | −71 to −89 | 0.0–0.4% in three provinces |
| POPU.TRE (Aw) | 81.5 (61–138) | 27–28 | −33 to −110 | 0.0–4.6% in two provinces |

These are endpoint maxima over the native support, not demonstrated culmination
ages. Only 0.5% of MGM group maxima hit the 350-year right endpoint; the rest
are interior maxima. The large difference from RSYC's 22–28-year MAI age is
still a shape signal, but it is not a calibration result.

## 5. Holdout evaluation and correction-factor status

The planning holdout protocol was implemented as a leave-one-unit-out level
multiplier evaluation:

| Dataset | Holdout unit | Evaluable units | Holdout rows | Aggregate bias before | After | Median unit abs bias before | After | Units improved | Materially improved |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BC FAIB | TSA | 38 | 18,482 | −30.9% | −1.8% | 33.8% | 15.9% | 71.1% | 63.2% |
| QC BFEC | unit | 5 | 690 | +6.8% | −0.6% | 27.2% | 34.2% | 60.0% | 20.0% |
| MGM | FMU | 0 | 0 | n/a | n/a | n/a | n/a | n/a | n/a |

Interpretation:

- The BC proxy is encouraging at the aggregate level, but it is not a
  predeclared fixed split and it is fitted within ecoprovince × species strata
  that can contain few TSAs. It is evidence for a future protocol, not a release
  test.
- The QC proxy improves the pooled mean but makes the median unit error worse
  and materially improves only 1 of 5 units. Unit-level QC factors do not
  generalise.
- MGM cannot be held out by FMU because the pinned CSVs have no FMU key.

`local_correction_factors.csv` contains 33 candidate rows (BC and QC only; no
MGM numeric factors). Every row has `status = withheld` and
`release_decision = not_released_pending_predeclared_holdout`. **No correction
factor is defensible now.** The correct next step is a predeclared whole-TSA /
whole-unit split, plus an MGM FMU key or an explicit decision to treat MGM as a
non-calibration screen.

## 6. Verification

- Focused tests: `.venv/bin/python -m pytest tests/test_rsyc_benchmark.py -q`
  → **18 passed**.
- Lint: `.venv/bin/ruff check workflows/national/rsyc_benchmark tests/test_rsyc_benchmark.py`
  → pass; `ruff format --check` → pass.
- Full benchmark rerun:
  `.venv/bin/python -m workflows.national.rsyc_benchmark.benchmark --out-dir data/derived/national/rsyc_benchmark --mgm-dir ../external/mgm`
  → exit 0.
- Outputs are under `data/derived/national/rsyc_benchmark/`.
- No commit was made.

## 7. Caveats and missing keys

- **No AGB benchmark.** The benchmark tests volume only. RSYC AGB is not
  validated here.
- **No RSYC height-age model.** The catalogue has volume and AGB only. Top
  height is MGM/BC/QC-reported and cannot be compared with RSYC.
- **BC volume definition.** BC FAIB source volume and RSYC volume may differ in
  utilisation/bark; part of the coastal negative bias may be definitional.
  Multi-plot visits with unallocated volume were excluded.
- **BC geography.** TSA→dominant VRI ecoprovince is coarse; 1,544 matched
  visits use the BEC fallback. The CWH fallback default is a coarse coastal
  assignment and can mix north- and south-coast stands. Fallback rows are
  grouped separately and should not be read as clean ecoprovince estimates.
- **QC unit key.** Unit→region→ecoprovince is based on the sample report, not
  unit geometry. The Gaspé/Mauricie results are unit-level evidence, not precise
  ecoprovince estimates.
- **QC curves are managed AAC outputs.** They are not unmanaged observations;
  67% are flat at age 50 and 100% at ages 100/150. The age-50 total comparison
  is the most defensible QC metric.
- **MGM equation verified, MGM geography not.** The functional form is now
  verified against the pinned loader. The benchmark still has no MGM FMU key
  and evaluates RSYC over all ecoprovinces in each province, including
  non-boreal parts. MGM results are a province-level screen, not a calibration
  dataset.
- **MGM cohort structure.** The fixed-yield-group evaluation uses starting-age
  strata; the starting-age mix differs by target age. Do not read the age rows
  as a longitudinal trajectory of the same groups.
- **MGM MAI is an endpoint maximum.** Values at 350 are right-censored. The
  comparison is directional, not a rotation-age estimate.
- **Small samples.** Some MGM `Aw` age-150 rows are small (32 yield groups
  across four provinces; 3 in AB) and should not be used for calibration.

## 8. Output files

| File | Description |
|---|---|
| `rsyc_vs_bc.csv` | BC ecoprovince × match basis × species × age-bin metrics, leading-species and composite |
| `rsyc_vs_bc_visits.csv` | Visit-level BC pairs, fallback keys, and BA accounting |
| `rsyc_vs_qc.csv` | QC unit × age × component metrics, validated same-mix total and flagged components |
| `rsyc_vs_qc_curves.csv` | Curve-level QC pairs |
| `rsyc_vs_qc_zero_total.csv` | Zero-total rows kept as a separate stratum |
| `rsyc_vs_qc_invalid_mix.csv` | Invalid/mismatched mix rows (empty in this sample) |
| `rsyc_vs_mgm.csv` | MGM province × species × age volume metrics and MAI endpoint maxima |
| `rsyc_vs_mgm_curves.csv` | Curve-level MGM pairs |
| `benchmark_summary.json` | Machine-readable summary, fix status, and holdout results |
| `local_correction_factors.csv` | Candidate-only multipliers, all `status = withheld` |
| `manifest.json` | Input paths, sizes, SHA-256 hashes, output row counts |
| `benchmark_overview.png` | Three-panel BC/QC/MGM overview figure |
| `BENCHMARK_FIX_REPORT.md` | Issue-by-issue fix report for the independent review |
