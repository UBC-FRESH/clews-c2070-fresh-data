# RSYC Benchmark Fix Report

**Date:** 2026-11-18  
**Scope:** Response to the independent review of the RSYC national volume
benchmark. No commit was made. All outputs are under
`data/derived/national/rsyc_benchmark/`.

## 1. Issue-by-issue status

| Review issue | Status | Evidence |
|---|---|---|
| 1. MGM equation unverified; cohort filter; MAI endpoint | **Fixed** | Equation verified against `UBC-FRESH/spades_ws3` commit `1847872` (`python/spadesws3.py`, `bootstrap_yields.f`); cohort filter removed; MAI reported as native-support endpoint maximum with censoring status |
| 2. QC zero-total / fabricated 50/50 mix | **Fixed** | Components validated finite/non-negative and mass-balanced; zero totals moved to `rsyc_vs_qc_zero_total.csv`; no fabricated mix; hit-rate denominators published |
| 3. BC fallback geography, BEC slicing, composite BA | **Fixed** | Explicit BEC zone/subzone parser; fallback stratum validated and retained; metrics grouped by resolved stratum + match basis; total/code-mapped/curve-resolved/group BA reported; unknown BA kept in denominator |
| 4. AGB claim too broad | **Fixed** | Report narrowed to volume-only exploratory; no AGB validation claim |
| 5. Holdout protocol not evaluated; correction factors promoted | **Fixed for evaluation; factors withheld** | Leave-one-unit-out holdout implemented for BC and QC; MGM not evaluable (no FMU key); `local_correction_factors.csv` all `status = withheld` |

## 2. MGM verification and corrections

### Verified source

- Repository: `https://github.com/UBC-FRESH/spades_ws3`
- Commit: `1847872` (`184787233aaa761f7b3eda54155d9dbbe50bf779`, 2022-03-30)
- File: `python/spadesws3.py`
- Function: `bootstrap_yields.f`
- Expression: `a * pow(x, b) * math.exp(-c * x)`
- Age origin: 0; age units: years
- Native support: 0–350 years, 10-year period
- Total volume: `cvol + dvol` via `_SUM`
- Fetched file SHA-256: `2b591065c25869a48d4a396edfb2502e78013ae44228abcb6847a2ecd3eea590`
- Working copy: `tmp/rsyc_review/spadesws3_1847872.py` (not committed)

The benchmark equation is exactly
`c_a*Age^c_b*exp(-c_c*Age) + d_a*Age^d_b*exp(-d_c*Age)`. The earlier “assumed
form” note is removed.

### Cohort fix

Old filter: `Age == age_encoded_in_ygrp`, which kept only each yield group's
starting row and changed the cohort at each target age. New rule: evaluate each
fixed yield group at every requested age inside its stored 31-year window.
`starting_age`, `starting_age_stratum`, `age_offset_min/max`, and
`n_starting_age_cohorts` are retained. The report labels MGM results as
starting-age strata, not a longitudinal trajectory.

### MAI fix

Old code computed argmax over ages 1–150 and called it “culmination”, making
150 an artificial endpoint. New code computes the endpoint maximum over MGM's
native 0–350-year support and records `mgm_mai_status`
(`interior_max`, `left_censored_at_1`, `right_censored_at_native_max`). The
report uses “endpoint maximum”, not “culmination”. In this sample 0.5% of group
maxima are right-censored at 350.

## 3. QC zero-total / mix fix

The old vectorised calculation used
`np.divide(..., out=0.5, where=total > 0)`, which gave a fabricated 50/50 mix to
zero-total rows. Example removed: unit 3152, `tbl_dde1384a6d55`, received
162.77 m³/ha at age 50 despite observed total 0.

New `derive_qc_mix(conifer, deciduous, total)` classifies each row:

- `positive_total`: finite, non-negative, balanced, total > 0; shares derived
  from the observed components;
- `zero_total`: finite, non-negative, balanced, total == 0; no mix, separate
  CSV;
- `invalid_components`: non-finite or negative;
- `mass_balance_mismatch`: components do not sum to total.

At target ages 50/100/150: 693 rows, 690 positive totals, 3 zero totals, 0
invalid/mismatched. Totals use n = 230 curves per age. `n_positive_observed` is
published for every metric row; hit rates use only positive observations.
`rsyc_vs_qc_zero_total.csv` and `rsyc_vs_qc_invalid_mix.csv` are emitted.

## 4. BC fallback geography and BA fix

- Explicit BEC parser with longest-zone-first matching and subzone retention:
  `CWHvm1 → CWH/vm`, `CHxw → CH/xw`, `MHmm1 → MH/mm`, `SBPSmc → SBPS/mc`.
  Unknown labels (`CMAunp`) stay unresolved.
- `resolve_bc_geography()` validates the TSA-dominant stratum first, then the
  BEC fallback against the area-weight stratum keys. Fallback visits retain a
  real `ecoprovince`, `ecoprovince_stratum`, `ecoprovince_mapping`, and
  `ecoprovince_detail`.
- All 1,544 matched fallback visits now have non-null ecoprovince. Metrics are
  grouped by ecoprovince and match basis; fallback rows are separate from
  TSA-dominant rows.
- `CompositePrediction` reports total BA, code-mapped BA, curve-resolved BA,
  species-resolved BA, group-resolved BA, code-unmapped BA, and
  curve-unresolved BA. The primary composite divides by total BA, so unknown
  BA remains in the denominator; the curve-resolved-only value is reported
  separately.

BA totals over 19,536 matched visits: 935,457.8 total; 914,494.2 code-mapped
(97.8%); 914,494.2 curve-resolved (97.8%); 20,963.6 code-unmapped (2.2%, kept
in denominator); 0 curve-unresolved. 6,727 visits contain some code-unmapped
BA.

## 5. Revised headline metrics

### BC FAIB

| Metric | Value |
|---|---:|
| Matched visits | 19,536 |
| Observed / RSYC (m³/ha) | 430 / 290 |
| Composite bias | −32.4% |
| Composite relative RMSE | 82.6% |
| Correlation | 0.59 |
| Within ±20% / ±30% | 18.7% / 28.8% |
| Fallback visits with non-null ecoprovince | 1,544 |

Age-bin composite bias: 40–60 −16.4%; 80–100 −36.3%; 120–140 −45.6%.

### QC BFEC

| Age | Positive curves | Observed | RSYC | Bias | Rel. RMSE | Within ±20% |
|---:|---:|---:|---:|---:|---:|---:|
| 50 | 230 | 171 | 160 | −6.7% | 41.7% | 37.0% |
| 100 | 230 | 171 | 194 | +13.4% | 42.9% | 37.0% |
| 150 | 230 | 171 | 195 | +13.9% | 43.1% | 37.4% |

Zero-total rows: 3 (one table, ages 50/100/150), excluded from totals. Invalid
mix rows: 0.

### MGM

Equation status: **verified**. Benchmark remains a province-level screen (no
FMU key). Volume rows: 47; median absolute relative bias 53.7%; mean within ±20%
13.1%. MAI endpoint rows: 16; median MGM endpoint age 116.5 years versus RSYC
27.5 years; 0.5% right-censored at 350. These are endpoint maxima, not
culmination ages, and are not calibration-grade.

## 6. Holdout and correction factors

The planning holdout protocol (`planning/national-rsyc-backbone.md` §5.2) was
implemented as a leave-one-unit-out level-multiplier evaluation:

| Dataset | Unit | Evaluable units | Holdout rows | Bias before | After | Median unit abs bias before | After | Units improved | Materially improved |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BC | TSA | 38 | 18,482 | −30.9% | −1.8% | 33.8% | 15.9% | 71.1% | 63.2% |
| QC | BFEC unit | 5 | 690 | +6.8% | −0.6% | 27.2% | 34.2% | 60.0% | 20.0% |
| MGM | FMU | 0 | 0 | n/a | n/a | n/a | n/a | n/a | n/a |

The BC proxy is encouraging but is not a predeclared fixed split. The QC proxy
improves the pooled mean but makes the median unit error worse and materially
improves only one unit. MGM cannot be held out by FMU. Therefore:

- `local_correction_factors.csv` is a candidate table only, 33 rows (BC/QC; no
  MGM numeric factors).
- Every row has `status = withheld` and
  `release_decision = not_released_pending_predeclared_holdout`.
- **No correction factor is defensible now.**

## 7. Tests added

`tests/test_rsyc_benchmark.py` now includes fixtures for:

1. **BC fallback / partial-BA visit**:
   `test_bc_fallback_visit_and_partial_ba_composite` — `MHmm1` fallback resolves
   to a non-null northern coastal stratum, and a mixture with 10% unknown BA
   keeps that BA in the composite denominator while reporting code-mapped and
   curve-resolved BA separately. `test_parse_bec_zone_handles_two_and_three_letter_zones`
   covers `CH`, `MH`, `CWH`, and `SBPS`.
2. **QC zero / invalid mix**:
   `test_qc_mix_zero_total_is_separate_and_invalid_mix_rejected` — zero total is
   `zero_total` with no shares; negative/non-finite components are
   `invalid_components`; mass mismatch is `mass_balance_mismatch`; balanced
   positive rows get observed shares.
3. **MGM yield group spanning multiple ages**:
   `test_mgm_target_rows_keep_fixed_group_across_supported_ages` — a group
   starting at 80 is evaluated at age 100 with offset 20, not dropped by the old
   `Age == starting_age` filter.
4. **Hit-rate denominator**:
   `test_regression_metrics_publishes_positive_hit_rate_denominator` — zero
   observed rows are excluded from the hit-rate denominator.
5. **MGM censoring**:
   `test_mgm_mai_endpoint_is_censored_at_native_maximum` — a monotone MAI curve
   returns `right_censored_at_native_max` at 350.

Run result: `.venv/bin/python -m pytest tests/test_rsyc_benchmark.py -q` →
**18 passed**.

## 8. Verification and paths

- Lint: `.venv/bin/ruff check workflows/national/rsyc_benchmark tests/test_rsyc_benchmark.py`
  → pass.
- Format: `.venv/bin/ruff format --check workflows/national/rsyc_benchmark tests/test_rsyc_benchmark.py`
  → pass.
- Benchmark rerun: exit 0, 36–43 s.
- Updated outputs:
  - `data/derived/national/rsyc_benchmark/RSYC_BENCHMARK_REPORT.md`
  - `data/derived/national/rsyc_benchmark/BENCHMARK_FIX_REPORT.md`
  - `data/derived/national/rsyc_benchmark/benchmark_summary.json`
  - `data/derived/national/rsyc_benchmark/rsyc_vs_bc.csv`
  - `data/derived/national/rsyc_benchmark/rsyc_vs_bc_visits.csv`
  - `data/derived/national/rsyc_benchmark/rsyc_vs_qc.csv`
  - `data/derived/national/rsyc_benchmark/rsyc_vs_qc_curves.csv`
  - `data/derived/national/rsyc_benchmark/rsyc_vs_qc_zero_total.csv`
  - `data/derived/national/rsyc_benchmark/rsyc_vs_qc_invalid_mix.csv`
  - `data/derived/national/rsyc_benchmark/rsyc_vs_mgm.csv`
  - `data/derived/national/rsyc_benchmark/rsyc_vs_mgm_curves.csv`
  - `data/derived/national/rsyc_benchmark/local_correction_factors.csv`
  - `data/derived/national/rsyc_benchmark/manifest.json`
  - `data/derived/national/rsyc_benchmark/benchmark_overview.png`

No commit was made.
