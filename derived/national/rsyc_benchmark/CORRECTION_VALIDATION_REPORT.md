# RSYC Correction Validation Report

**Date:** 2026-11-19  
**Scope:** Full BC FAIB PSP benchmark and full QC BFEC public extraction.  
**Status:** Predeclared holdout validation complete. No correction has been
applied to the 119M/150M/100M/200M supply artifacts and no C2070 run was
repeated.

## 1. Protocol (predeclared)

The split and decision rule were fixed before fitting:

- **BC:** 20% of TSAs held out, stratified by ecoprovince, seed `20261119`.
  Whole TSAs are the independent unit. 8 of
  40 usable TSAs were held out:
  Cranbrook, Kalum, Kamloops, Kingcome, Pacific, Prince George, Robson Valley, Williams Lake.
- **QC:** 20% of public non-restricted BFEC units held out, stratified by
  administrative region, seed `20261119`. Whole units are the independent unit.
  Every region with at least two units contributes at least one held-out unit,
  so the realised share is 12 of 51 usable
  units (23.5%):
  01171, 02751, 03152, 03453, 04352, 06151, 06252, 07151, 08251, 08751, 09452, 11262.
- **Fit:** a single multiplicative `b1` scalar per stratum, fitted by least
  squares through the origin on training units only:
  `b = sum(observed*predicted) / sum(predicted^2)`. The ratio-of-sums scalar is
  reported as a diagnostic. No zero, negative, or non-finite observation is
  used.
- **BC stratum:** `ecoprovince_stratum × leading_species`, ages
  40–150 years, on the BA-weighted composite prediction.
- **QC stratum:** `ecoprovince proxy × total`, target ages 50/100/150, on the
  same-mix RSYC total prediction. The ecoprovince proxy is required because no
  public unit→ecoprovince join exists (see §6).
- **Support:** at least 30 training rows and 2
  training units; at least 30 held-out rows and 1
  held-out unit. Strata below either threshold are `insufficient_support`.
- **Decision:** `validated` only when held-out `|bias|` falls by at least 50%
  and held-out relative RMSE does not worsen by more than 5% (relative).
  Otherwise `withheld`. A separate `material` flag marks strata whose
  held-out pre-correction `|bias|` is at least 10%.
- **Secondary:** leave-one-TSA-out (BC) and leave-one-unit-out (QC) are
  reported for every candidate stratum. They are a robustness check, not a
  substitute for the predeclared split.
- **Release gate:** a primary-validated factor is recommended for application
  only if the leave-one-unit-out check has at least 3 folds, a
  median bias reduction of at least 50%, and at least half the folds within
  the 5% RMSE tolerance. This is an additional conservatism; it does not
  change the `status` column defined by the primary rule.

## 2. BC result

BC exclusions: 41 visits have no TSA and
1,424 are outside the 40–150 age window
(overlaps counted once), leaving 18,081 usable visits.

**Aggregate held-out composite volume:**

| stratum_level | n_test | n_test_units | coverage_rows | coverage_share | test_before_bias | test_after_bias | bias_reduction | test_before_relative_rmse | test_after_relative_rmse | rel_rmse_change | test_before_within20 | test_after_within20 | test_before_within30 | test_after_within30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| aggregate_release_policy_all_test_rows | 3545 | 8 | 1071 | 0.3021 | -0.1436 | 0.08061 | 0.4388 | 0.807 | 0.6193 | -0.2327 | 0.1938 | 0.2629 | 0.2931 | 0.3856 |
| aggregate_release_policy_covered_test_rows | 1071 | 5 | 1071 | 0.3021 | -0.3813 | 0.06377 | 0.8328 | 0.7024 | 0.4178 | -0.4051 | 0.155 | 0.3838 | 0.2446 | 0.5509 |
| aggregate_all_candidate_factors_all_test_rows | 3545 | 8 | 3433 | 0.9684 | -0.1436 | 0.09447 | 0.3423 | 0.807 | 0.5661 | -0.2986 | 0.1938 | 0.27 | 0.2931 | 0.4008 |


The release policy covers 30.2% of held-out
visits. On that covered subset the absolute bias falls by
83.3% and relative RMSE by
40.5%; the all-visit aggregate falls
less (43.9% bias,
23.3% RMSE) because the uncovered
interior strata remain uncorrected. The all-candidate diagnostic over-corrects
and is not a release option.

**Per-ecoprovince (all species pooled) diagnostic:**

| stratum_key | multiplier | n_train | n_test | n_test_units | test_before_bias | test_after_bias | bias_reduction | rel_rmse_change | status |
|---|---|---|---|---|---|---|---|---|---|
| Pacific Maritime/Southern Coastal Mountains | 2.177 | 6447 | 683 | 3 | -0.5212 | 0.04235 | 0.9188 | -0.4114 | validated |
| Montane Cordillera/Southern Montane Cordillera | 0.9607 | 2703 | 951 | 1 | 0.2569 | 0.2075 | 0.1923 | -0.02517 | withheld |
| Montane Cordillera/Columbia Montane Cordillera | 1.085 | 2229 | 623 | 2 | 0.4665 | 0.591 | -0.2668 | 0.0929 | withheld |
| Montane Cordillera/Central Montane Cordillera | 0.9767 | 1372 | 485 | 1 | 0.2865 | 0.2565 | 0.1047 | -0.01208 | withheld |
| Montane Cordillera/Northern Montane Cordillera | 1.222 | 1229 | 803 | 1 | -0.1643 | 0.02097 | 0.8724 | -0.04441 | validated |
| Boreal Plains/Boreal Foothills | 1.032 | 213 | 0 | 0 |  |  |  |  | insufficient_support |
| Boreal Cordillera/Southern Boreal Cordillera |  | 21 | 0 | 0 |  |  |  |  | insufficient_support |
| Taiga Plains/Hay-Slave Lowlands | 1.891 | 322 | 0 | 0 |  |  |  |  | insufficient_support |


**Age-bin diagnostic for the release-policy factors (held-out, no age floor):**

| stratum_key | n_test | n_test_units | coverage_share | test_before_bias | test_after_bias | bias_reduction | test_before_relative_rmse | test_after_relative_rmse | rel_rmse_change | test_before_within20 | test_after_within20 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 101-119 | 514 | 7 | 0.2568 | -0.1631 | 0.02802 | 0.8282 | 0.8197 | 0.6104 | -0.2554 | 0.1634 | 0.2315 |
| 120-140 | 366 | 7 | 0.2814 | -0.2377 | -0.07029 | 0.7043 | 0.8361 | 0.65 | -0.2225 | 0.1995 | 0.2842 |
| 141-150 | 113 | 7 | 0.3717 | -0.2917 | -0.05728 | 0.8036 | 0.7376 | 0.4804 | -0.3487 | 0.2035 | 0.3805 |
| 40-60 | 631 | 8 | 0.2979 | 0.03685 | 0.3658 | -8.925 | 0.8002 | 0.8018 | 0.002031 | 0.1791 | 0.2029 |
| 61-79 | 1010 | 8 | 0.3228 | -0.1531 | 0.09007 | 0.4119 | 0.7473 | 0.5292 | -0.2919 | 0.2198 | 0.2911 |
| 80-100 | 911 | 8 | 0.3074 | -0.1397 | 0.06115 | 0.5623 | 0.8143 | 0.6148 | -0.245 | 0.1888 | 0.2678 |


The level scalar is age-blind. Applied without an age floor it over-corrects
the 40–60 bin (bias +3.7% to +36.6%) while
improving every bin from 61–79 upward. The recommended application floor is
therefore 61 years; the 40–60 bin is left uncorrected.

**Primary-rule validated strata (10):**

| stratum_key | multiplier | n_train | n_test | n_test_units | test_before_bias | test_after_bias | bias_reduction | test_before_relative_rmse | test_after_relative_rmse | rel_rmse_change | lo_folds | lo_median_bias_reduction | lo_share_folds_bias_reduced | lo_robust |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Montane Cordillera/Columbia Montane Cordillera|LARI.OCC | 0.6715 | 214 | 135 | 1 | 1.019 | 0.3556 | 0.651 | 1.133 | 0.5909 | -0.4787 | 4 | 0.7656 | 1 | True |
| Montane Cordillera/Northern Montane Cordillera|PICE.GLA | 1.287 | 244 | 340 | 1 | -0.1695 | 0.0692 | 0.5917 | 0.4128 | 0.3797 | -0.08004 | 3 | 0.9412 | 1 | True |
| Montane Cordillera/Northern Montane Cordillera|PINU.CON | 1.349 | 555 | 191 | 1 | -0.3464 | -0.1185 | 0.6579 | 0.5604 | 0.4573 | -0.1838 | 2 | -0.4397 | 0.5 | False |
| Montane Cordillera/Northern Montane Cordillera|POPU.TRE | 1.104 | 288 | 110 | 1 | -0.09163 | 0.003091 | 0.9663 | 0.7228 | 0.7146 | -0.01132 | 2 | 0.6712 | 1 | False |
| Montane Cordillera/Southern Montane Cordillera|PINU.CON | 1.221 | 681 | 165 | 1 | -0.1746 | 0.008158 | 0.9533 | 0.3908 | 0.3489 | -0.1072 | 4 | -0.7942 | 0 | False |
| Montane Cordillera/Southern Montane Cordillera|PSEU.MEN | 0.8126 | 1418 | 596 | 1 | 0.4375 | 0.1681 | 0.6158 | 0.844 | 0.7291 | -0.1361 | 3 | 0.1572 | 0.6667 | False |
| Pacific Maritime/Southern Coastal Mountains|ABIE.AMA | 2.09 | 257 | 62 | 2 | -0.557 | -0.07394 | 0.8672 | 0.7383 | 0.4718 | -0.361 | 4 | 0.3546 | 0.75 | False |
| Pacific Maritime/Southern Coastal Mountains|PSEU.MEN | 2.002 | 2185 | 73 | 1 | -0.4933 | 0.01423 | 0.9712 | 0.6631 | 0.425 | -0.3591 | 8 | 0.6548 | 1 | True |
| Pacific Maritime/Southern Coastal Mountains|THUJ.PLI | 2.131 | 468 | 38 | 3 | -0.5352 | -0.009475 | 0.9823 | 0.6946 | 0.4126 | -0.406 | 9 | 0.776 | 0.6667 | True |
| Pacific Maritime/Southern Coastal Mountains|TSUG.HET | 2.178 | 2491 | 485 | 3 | -0.5173 | 0.05125 | 0.9009 | 0.6344 | 0.3666 | -0.4221 | 11 | 0.5867 | 0.6364 | True |


**Recommended for application after LO-TSA robustness (5):**
a primary validation is downgraded when the leave-one-TSA-out check does not
show a median bias reduction of at least 50% or does not keep at least half of
the folds within the 5% RMSE tolerance.

| stratum_key | multiplier | n_train | n_test | n_test_units | test_before_bias | test_after_bias | bias_reduction | rel_rmse_change | lo_folds | lo_median_bias_reduction | lo_share_folds_bias_reduced | lo_share_folds_rmse_ok |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Montane Cordillera/Columbia Montane Cordillera|LARI.OCC | 0.6715 | 214 | 135 | 1 | 1.019 | 0.3556 | 0.651 | -0.4787 | 4 | 0.7656 | 1 | 1 |
| Montane Cordillera/Northern Montane Cordillera|PICE.GLA | 1.287 | 244 | 340 | 1 | -0.1695 | 0.0692 | 0.5917 | -0.08004 | 3 | 0.9412 | 1 | 1 |
| Pacific Maritime/Southern Coastal Mountains|PSEU.MEN | 2.002 | 2185 | 73 | 1 | -0.4933 | 0.01423 | 0.9712 | -0.3591 | 8 | 0.6548 | 1 | 1 |
| Pacific Maritime/Southern Coastal Mountains|THUJ.PLI | 2.131 | 468 | 38 | 3 | -0.5352 | -0.009475 | 0.9823 | -0.406 | 9 | 0.776 | 0.6667 | 0.7778 |
| Pacific Maritime/Southern Coastal Mountains|TSUG.HET | 2.178 | 2491 | 485 | 3 | -0.5173 | 0.05125 | 0.9009 | -0.4221 | 11 | 0.5867 | 0.6364 | 0.6364 |


**Validated by the primary rule but not released after the LO check
(5; unstable or fewer than 3 folds):**

| stratum_key | multiplier | n_test | n_test_units | test_before_bias | test_after_bias | bias_reduction | rel_rmse_change | lo_folds | lo_median_bias_reduction | lo_share_folds_bias_reduced |
|---|---|---|---|---|---|---|---|---|---|---|
| Montane Cordillera/Northern Montane Cordillera|PINU.CON | 1.349 | 191 | 1 | -0.3464 | -0.1185 | 0.6579 | -0.1838 | 2 | -0.4397 | 0.5 |
| Montane Cordillera/Northern Montane Cordillera|POPU.TRE | 1.104 | 110 | 1 | -0.09163 | 0.003091 | 0.9663 | -0.01132 | 2 | 0.6712 | 1 |
| Montane Cordillera/Southern Montane Cordillera|PINU.CON | 1.221 | 165 | 1 | -0.1746 | 0.008158 | 0.9533 | -0.1072 | 4 | -0.7942 | 0 |
| Montane Cordillera/Southern Montane Cordillera|PSEU.MEN | 0.8126 | 596 | 1 | 0.4375 | 0.1681 | 0.6158 | -0.1361 | 3 | 0.1572 | 0.6667 |
| Pacific Maritime/Southern Coastal Mountains|ABIE.AMA | 2.09 | 62 | 2 | -0.557 | -0.07394 | 0.8672 | -0.361 | 4 | 0.3546 | 0.75 |


**Withheld strata (8):** these failed the bias-reduction or
RMSE rule.

| stratum_key | multiplier | n_train | n_test | n_test_units | test_before_bias | test_after_bias | bias_reduction | rel_rmse_change | reason |
|---|---|---|---|---|---|---|---|---|---|
| Montane Cordillera/Central Montane Cordillera|PINU.CON | 1.261 | 877 | 159 | 1 | 0.1272 | 0.4214 | -2.312 | 0.1054 | bias_reduction_below_50pct;relative_rmse_worsened_over_5pct |
| Montane Cordillera/Central Montane Cordillera|PSEU.MEN | 0.4728 | 207 | 261 | 1 | 0.4098 | -0.3335 | 0.1863 | -0.034 | bias_reduction_below_50pct |
| Montane Cordillera/Columbia Montane Cordillera|ABIE.LAS | 0.8918 | 101 | 56 | 2 | 0.4417 | 0.2856 | 0.3533 | -0.1187 | bias_reduction_below_50pct |
| Montane Cordillera/Columbia Montane Cordillera|PINU.CON | 0.9475 | 457 | 203 | 2 | 0.4202 | 0.3457 | 0.1774 | -0.07527 | bias_reduction_below_50pct |
| Montane Cordillera/Columbia Montane Cordillera|PSEU.MEN | 1.083 | 691 | 133 | 2 | 0.4287 | 0.5468 | -0.2757 | 0.0761 | bias_reduction_below_50pct;relative_rmse_worsened_over_5pct |
| Montane Cordillera/Northern Montane Cordillera|ABIE.LAS | 0.9884 | 89 | 110 | 1 | 0.1507 | 0.1373 | 0.08873 | -0.006521 | bias_reduction_below_50pct |
| Montane Cordillera/Southern Montane Cordillera|ABIE.LAS | 1.218 | 91 | 86 | 1 | 0.6156 | 0.9683 | -0.5731 | 0.3293 | bias_reduction_below_50pct;relative_rmse_worsened_over_5pct |
| Montane Cordillera/Southern Montane Cordillera|PICE.ENG | 1.393 | 32 | 33 | 1 | 0.6192 | 1.255 | -1.026 | 0.6853 | bias_reduction_below_50pct;relative_rmse_worsened_over_5pct |


**Insufficient support (49):** single-TSA ecoprovinces
cannot be split, and several species strata had too few held-out visits.

| stratum_key | n_train | n_train_units | n_test | n_test_units | reason |
|---|---|---|---|---|---|
| Pacific Maritime/Southern Coastal Mountains|THUJ.OCC | 6 | 2 | 2 | 1 | train_rows_below_30 |
| Pacific Maritime/Southern Coastal Mountains|PICE.SIT | 614 | 6 | 18 | 1 | test_rows_below_30 |
| Pacific Maritime/Southern Coastal Mountains|ALNU.RUB | 152 | 8 | 0 | 0 | test_rows_below_30 |
| Pacific Maritime/Southern Coastal Mountains|POPU.BAL | 6 | 4 | 0 | 0 | train_rows_below_30 |
| Pacific Maritime/Southern Coastal Mountains|ACER.MAC | 27 | 3 | 0 | 0 | train_rows_below_30 |
| Pacific Maritime/Southern Coastal Mountains|PINU.CON | 152 | 3 | 5 | 3 | test_rows_below_30 |
| Montane Cordillera/Southern Montane Cordillera|POPU.TRE | 5 | 1 | 11 | 1 | train_rows_below_30 |
| Montane Cordillera/Southern Montane Cordillera|PINU.PON | 15 | 3 | 6 | 1 | train_rows_below_30 |
| Montane Cordillera/Southern Montane Cordillera|PICE.GLA | 107 | 4 | 25 | 1 | test_rows_below_30 |
| Montane Cordillera/Southern Montane Cordillera|THUJ.PLI | 123 | 2 | 8 | 1 | test_rows_below_30 |
| Montane Cordillera/Southern Montane Cordillera|LARI.OCC | 174 | 2 | 0 | 0 | test_rows_below_30 |
| Montane Cordillera/Columbia Montane Cordillera|THUJ.PLI | 214 | 4 | 5 | 2 | test_rows_below_30 |
| Montane Cordillera/Columbia Montane Cordillera|PICE.ENG | 38 | 5 | 17 | 1 | test_rows_below_30 |
| Montane Cordillera/Columbia Montane Cordillera|TSUG.HET | 280 | 5 | 6 | 1 | test_rows_below_30 |
| Montane Cordillera/Columbia Montane Cordillera|POPU.TRE | 35 | 6 | 5 | 2 | test_rows_below_30 |
| Montane Cordillera/Columbia Montane Cordillera|PICE.GLA | 180 | 6 | 29 | 2 | test_rows_below_30 |
| Montane Cordillera/Columbia Montane Cordillera|ABIE.AMA | 3 | 1 | 0 | 0 | train_rows_below_30 |
| Montane Cordillera/Columbia Montane Cordillera|PINU.PON | 15 | 2 | 32 | 1 | train_rows_below_30 |
| Montane Cordillera/Columbia Montane Cordillera|POPU.BAL | 1 | 1 | 2 | 2 | train_rows_below_30 |
| Montane Cordillera/Southern Montane Cordillera|TSUG.HET | 57 | 1 | 21 | 1 | train_units_below_2 |
| Montane Cordillera/Central Montane Cordillera|PICE.GLA | 150 | 4 | 24 | 1 | test_rows_below_30 |
| Montane Cordillera/Central Montane Cordillera|POPU.TRE | 51 | 3 | 15 | 1 | test_rows_below_30 |
| Montane Cordillera/Central Montane Cordillera|PINU.PON | 4 | 1 | 0 | 0 | train_rows_below_30 |
| Montane Cordillera/Central Montane Cordillera|ABIE.LAS | 62 | 4 | 19 | 1 | test_rows_below_30 |
| Montane Cordillera/Central Montane Cordillera|PICE.MAR | 13 | 2 | 0 | 0 | train_rows_below_30 |
| Montane Cordillera/Northern Montane Cordillera|PSEU.MEN | 5 | 1 | 42 | 1 | train_rows_below_30 |
| Montane Cordillera/Central Montane Cordillera|PICE.ENG | 8 | 2 | 2 | 1 | train_rows_below_30 |
| Montane Cordillera/Central Montane Cordillera|THUJ.PLI | 0 | 0 | 5 | 1 | train_rows_below_30 |
| Montane Cordillera/Northern Montane Cordillera|TSUG.HET | 0 | 0 | 2 | 1 | train_rows_below_30 |
| Montane Cordillera/Northern Montane Cordillera|POPU.BAL | 5 | 1 | 3 | 1 | train_rows_below_30 |
| Pacific Maritime/Southern Coastal Mountains|ABIE.LAS | 19 | 2 | 0 | 0 | train_rows_below_30 |
| Pacific Maritime/Southern Coastal Mountains|POPU.TRE | 59 | 1 | 0 | 0 | train_units_below_2 |
| Pacific Maritime/Southern Coastal Mountains|PICE.GLA | 11 | 1 | 0 | 0 | train_rows_below_30 |
| Montane Cordillera/Northern Montane Cordillera|PICE.MAR | 24 | 2 | 0 | 0 | train_rows_below_30 |
| Montane Cordillera/Northern Montane Cordillera|PICE.ENG | 19 | 2 | 5 | 1 | train_rows_below_30 |
| Boreal Plains/Boreal Foothills|PINU.CON | 109 | 1 | 0 | 0 | train_units_below_2 |
| Boreal Plains/Boreal Foothills|PICE.MAR | 20 | 1 | 0 | 0 | train_rows_below_30 |
| Boreal Plains/Boreal Foothills|POPU.TRE | 55 | 1 | 0 | 0 | train_units_below_2 |
| Boreal Plains/Boreal Foothills|PICE.GLA | 29 | 1 | 0 | 0 | train_rows_below_30 |
| Boreal Cordillera/Southern Boreal Cordillera|PINU.CON | 13 | 1 | 0 | 0 | train_rows_below_30 |
| Boreal Cordillera/Southern Boreal Cordillera|ABIE.LAS | 1 | 1 | 0 | 0 | train_rows_below_30 |
| Boreal Cordillera/Southern Boreal Cordillera|PICE.GLA | 7 | 1 | 0 | 0 | train_rows_below_30 |
| Taiga Plains/Hay-Slave Lowlands|POPU.TRE | 145 | 1 | 0 | 0 | train_units_below_2 |
| Taiga Plains/Hay-Slave Lowlands|PICE.GLA | 99 | 1 | 0 | 0 | train_units_below_2 |
| Taiga Plains/Hay-Slave Lowlands|PICE.MAR | 39 | 1 | 0 | 0 | train_units_below_2 |
| Taiga Plains/Hay-Slave Lowlands|ABIE.LAS | 5 | 1 | 0 | 0 | train_rows_below_30 |
| Taiga Plains/Hay-Slave Lowlands|POPU.BAL | 18 | 1 | 0 | 0 | train_rows_below_30 |
| Taiga Plains/Hay-Slave Lowlands|PINU.CON | 11 | 1 | 0 | 0 | train_rows_below_30 |
| Taiga Plains/Hay-Slave Lowlands|PINU.BAN | 5 | 1 | 0 | 0 | train_rows_below_30 |


BC reading: the coastal factors are the strongest and most stable result. The
Columbia larch and Northern Montane spruce factors also survive both the
predeclared split and leave-one-TSA-out. Several other species pass the primary
split but are downgraded because the leave-one-TSA-out check is unstable; the
Central Montane species are weak and the single-TSA Boreal Foothills /
Hay-Slave Lowlands strata cannot be validated at all.

## 3. QC result

**Aggregate held-out same-mix total volume:**

| stratum_level | n_test | n_test_units | coverage_rows | coverage_share | test_before_bias | test_after_bias | bias_reduction | test_before_relative_rmse | test_after_relative_rmse | rel_rmse_change | test_before_within20 | test_after_within20 | test_before_within30 | test_after_within30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| aggregate_release_policy_all_test_rows | 1707 | 12 | 0 | 0 | -0.1249 | -0.1249 | 0 | 0.3865 | 0.3865 | 0 | 0.3972 | 0.3972 | 0.5917 | 0.5917 |
| aggregate_all_candidate_factors_all_test_rows | 1707 | 12 | 1707 | 1 | -0.1249 | -0.03913 | 0.6867 | 0.3865 | 0.3687 | -0.04607 | 0.3972 | 0.4429 | 0.5917 | 0.618 |


The release policy applies no QC factor, so the all-visit before/after rows are
identical. The all-candidate diagnostic would cover all held-out rows and
reduce absolute bias by 68.7%, but four of
the five candidate strata are withheld and the remaining proxy fails the
leave-one-unit-out check; that aggregate is not a defensible release.

**All-candidate diagnostic by age (held-out):**

| stratum_key | n_test | n_test_units | coverage_share | test_before_bias | test_after_bias | bias_reduction | test_before_relative_rmse | test_after_relative_rmse | rel_rmse_change | test_before_within20 | test_after_within20 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 100 | 569 | 12 | 1 | -0.07065 | 0.02039 | 0.7114 | 0.3591 | 0.3521 | -0.01952 | 0.4569 | 0.4833 |
| 150 | 569 | 12 | 1 | -0.06697 | 0.0245 | 0.6343 | 0.3602 | 0.3544 | -0.01616 | 0.4534 | 0.4745 |
| 50 | 569 | 12 | 1 | -0.2368 | -0.162 | 0.3158 | 0.4351 | 0.3977 | -0.08588 | 0.2812 | 0.3708 |


**Ecoprovince-proxy strata (5):**

| stratum_key | multiplier | n_train | n_train_units | n_test | n_test_units | test_before_bias | test_after_bias | bias_reduction | rel_rmse_change | status | reason |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Atlantic Maritime/Appalachian-Acadian Highlands | 1.118 | 1215 | 6 | 615 | 3 | -0.1508 | -0.05053 | 0.6649 | -0.07518 | validated | passed_predeclared_rule |
| Boreal Shield East/Eastern Boreal Shield | 1.096 | 1116 | 11 | 168 | 2 | 0.1502 | 0.2603 | -0.7332 | 0.1224 | withheld | bias_reduction_below_50pct;relative_rmse_worsened_over_5pct |
| Boreal Shield East/Southern Boreal Shield | 1.059 | 2220 | 15 | 744 | 5 | -0.1346 | -0.08389 | 0.3767 | -0.03896 | withheld | bias_reduction_below_50pct |
| Boreal Shield East/Mid-Boreal Shield | 1.289 | 834 | 5 | 111 | 1 | -0.06031 | 0.2108 | -2.496 | 0.331 | withheld | bias_reduction_below_50pct;relative_rmse_worsened_over_5pct |
| Taiga Shield East/Eastern Taiga | 1.136 | 189 | 2 | 69 | 1 | -0.04386 | 0.08658 | -0.9742 | 0.02414 | withheld | bias_reduction_below_50pct |


**Primary-rule validated proxy strata (1):**

| stratum_key | multiplier | n_train | n_test | n_test_units | test_before_bias | test_after_bias | bias_reduction | test_before_relative_rmse | test_after_relative_rmse | rel_rmse_change | lo_folds | lo_median_bias_reduction | lo_share_folds_bias_reduced | lo_robust |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Atlantic Maritime/Appalachian-Acadian Highlands | 1.118 | 1215 | 615 | 3 | -0.1508 | -0.05053 | 0.6649 | 0.3696 | 0.3418 | -0.07518 | 6 | 0.228 | 0.6667 | False |


**Recommended for application after LO-unit robustness (0):**

_No rows._


**Administrative-region diagnostics (13 rows, all single-unit
test sets):** these are descriptive only because most regions contribute one
held-out unit.

| region | ecoprovince_proxy | multiplier | n_test | n_test_units | test_before_bias | test_after_bias | bias_reduction | rel_rmse_change | status |
|---|---|---|---|---|---|---|---|---|---|
| R01 | Atlantic Maritime/Appalachian-Acadian Highlands | 1.241 | 282 | 1 | -0.2467 | -0.06493 | 0.7368 | -0.2241 | insufficient_support |
| R02 | Boreal Shield East/Eastern Boreal Shield | 1.203 | 90 | 1 | 0.03417 | 0.2436 | -6.129 | 0.2163 | withheld |
| R03 | Boreal Shield East/Southern Boreal Shield | 0.8726 | 165 | 1 | 0.2171 | 0.06205 | 0.7142 | -0.1108 | validated |
| R04 | Boreal Shield East/Southern Boreal Shield | 0.8975 | 114 | 1 | 0.1131 | -0.001024 | 0.9909 | -0.07021 | validated |
| R05 | Atlantic Maritime/Appalachian-Acadian Highlands | 1.203 | 0 | 0 |  |  |  |  | insufficient_support |
| R07 | Boreal Shield East/Southern Boreal Shield | 1.138 | 183 | 1 | -0.2695 | -0.1684 | 0.3749 | -0.1765 | withheld |
| R08 | Boreal Shield East/Mid-Boreal Shield | 1.289 | 111 | 1 | -0.06031 | 0.2108 | -2.496 | 0.331 | withheld |
| R09 | Boreal Shield East/Eastern Boreal Shield | 0.9286 | 78 | 1 | 0.3228 | 0.2283 | 0.2927 | -0.1039 | withheld |
| R10 | Taiga Shield East/Eastern Taiga | 1.136 | 69 | 1 | -0.04386 | 0.08658 | -0.9742 | 0.02414 | withheld |
| R11 | Atlantic Maritime/Appalachian-Acadian Highlands | 0.8363 | 183 | 1 | 0.1125 | -0.06965 | 0.3808 | -0.01932 | withheld |
| R12 | Atlantic Maritime/Appalachian-Acadian Highlands | 1.218 | 150 | 1 | -0.1781 | 0.001131 | 0.9937 | -0.1669 | validated |
| R14 | Boreal Shield East/Southern Boreal Shield | 1.316 | 120 | 1 | -0.03357 | 0.2721 | -7.107 | 0.4667 | insufficient_support |
| R15 | Boreal Shield East/Southern Boreal Shield | 1.21 | 162 | 1 | -0.3328 | -0.1924 | 0.4218 | -0.2694 | withheld |


QC reading: only the Appalachian proxy passes the primary split, and it is
downgraded by the leave-one-unit-out check: the median fold bias reduction is
22.8% and only one of six folds reaches 50%. Southern Boreal Shield misses the
50% primary threshold (37.7%). Eastern Boreal Shield, Mid-Boreal Shield and
Eastern Taiga are withheld. The administrative-region table shows the same
instability: some regions improve strongly, others reverse sign or worsen
RMSE, and every region test is a single held-out unit. The QC correction layer
is therefore not recommended for release.

## 4. Recommendation

**Apply BC-only**

BC has 10 strata that pass the predeclared holdout rule; 5 of them also survive the leave-one-TSA-out check and are recommended for application. The BC scalar is age-blind: in the held-out 40-60 bin applying it without an age floor would move bias from +3.7% to +36.6%; the recommended application floor is 61 years, so the 40-60 bin stays uncorrected. QC has 1 proxy strata that pass the primary rule, but 0 survive leave-one-unit-out. The QC proxy is also not a spatial unit→ecoprovince join: the public BFEC crosswalk has no coordinates and no published eco-code lookup. Release the recommended BC strata only, at ages >=61; keep every QC factor as a candidate until BFEC geometry or a published eco-code crosswalk is available. Do not apply any withheld, insufficient-support, or validated-primary-only-lo-unstable stratum.

The released set is limited to strata with `status=validated` **and**
`lo_robust=true`; every other stratum remains `withheld`,
`insufficient_support`, or `validated_primary_only_lo_unstable`. No factor was
applied in this task.

## 5. Tests, paths and status

| Item | Value |
|---|---|
| Validation script | `workflows/national/rsyc_benchmark/validate_corrections.py` |
| BC input | `data/derived/national/rsyc_benchmark/rsyc_vs_bc_visits.csv` |
| QC inputs | `data/derived/national/qc_bfec_full/qc_bfec_curves.csv`, `data/derived/national/qc_bfec_full/qc_bfec_development_types.csv`, `data/derived/national/qc_bfec_full/qc_bfec_manifest.json` |
| RSYC models | `data/raw/national/rsyc/RSYC_models.zip` |
| National fit | `data/derived/national/assortments/national_fit/national_distribution_parameters.csv` |
| Validation table | `data/derived/national/rsyc_benchmark/correction_validation.csv` |
| Validated/candidate table | `data/derived/national/rsyc_benchmark/local_correction_factors_validated.csv` |
| Summary | `data/derived/national/rsyc_benchmark/correction_validation_summary.json` |
| Manifest | `data/derived/national/rsyc_benchmark/correction_validation_manifest.json` |
| BC visits used | 18,081 of 19,536 |
| QC positive curve-age rows | 7,281 |
| QC zero-total rows excluded | 93 |
| QC invalid rows excluded | 0 |
| Verification | `ruff check` pass; `py_compile` pass |
| 119M/150M/100M/200M artifacts | not modified |
| C2070 rerun | not performed |

The validation manifest is named `correction_validation_manifest.json` rather
than `manifest.json` so the existing benchmark manifest is not overwritten.

## 6. Caveats

**QC unit→ecoprovince join is a proxy, not a spatial join.** The public BFEC
inventory crosswalk has columns `unit`, `polygon_id`, `THEME1`–`THEME20`,
`STRATE`, `area_ha`, `CRS`; it has no X/Y centroid or polygon geometry.
`THEME20` carries `ecoNN` BFEC ecological-unit codes, but no published
`ecoNN` → Canadian ecodistrict/ecoprovince lookup is present in the repository
or the extraction manifest. The public bundle index supplies only the
administrative region (`R01`–`R15`). The QC factors therefore use the
administrative-region → ecoprovince proxy in
`QC_REGION_ECOPROVINCE_PROXY`, with per-region confidence recorded in the
summary JSON and in the `proxy_confidence` column:

| Region | Proxy ecoprovince | Confidence |
|---|---|---|
| R01 | Atlantic Maritime/Appalachian-Acadian Highlands | high |
| R02 | Boreal Shield East/Eastern Boreal Shield | medium |
| R03 | Boreal Shield East/Southern Boreal Shield | medium |
| R04 | Boreal Shield East/Southern Boreal Shield | high |
| R05 | Atlantic Maritime/Appalachian-Acadian Highlands | high |
| R07 | Boreal Shield East/Southern Boreal Shield | high |
| R08 | Boreal Shield East/Mid-Boreal Shield | medium |
| R09 | Boreal Shield East/Eastern Boreal Shield | medium |
| R10 | Taiga Shield East/Eastern Taiga | low |
| R11 | Atlantic Maritime/Appalachian-Acadian Highlands | high |
| R12 | Atlantic Maritime/Appalachian-Acadian Highlands | high |
| R14 | Boreal Shield East/Southern Boreal Shield | high |
| R15 | Boreal Shield East/Southern Boreal Shield | high |

R10 is the weakest proxy: it spans Eastern Taiga, Hudson-James Lowlands and
Mid-Boreal Shield. A true spatial join requires either BFEC polygon centroids
or a published BFEC eco-code crosswalk; neither is available here.

**The R03 proxy differs from the previous five-unit benchmark.** The earlier
sample mapped R03 to Atlantic Maritime/Appalachian-Acadian Highlands. This
validation maps R03 to Boreal Shield East/Southern Boreal Shield because the
R03 units are Laurentian/Charlevoix southern-boreal units. The re-mapping is
flagged as medium confidence. It changes the reconstructed prediction for the
two R03 sample units (3151 and 3152); the three units whose proxy matches the
earlier mapping (2651, 3451, 3551) reproduce the published benchmark
predictions exactly.

**BFEC curves are managed AAC tables.** Productive development types only
(`in_model=1`, `productive=1`, area>0) were used. Many curves are flat or
post-rotation at ages 100/150, so the age-50/100/150 scalar is a level
correction, not a rotation-age or shape correction. Zero-total and invalid
mass-balance rows were excluded rather than assigned a fabricated mix.

**Restricted units were excluded.** Units 06451, 08462 and 08562 carry
confidentiality notices; their public development-type aggregates and
inventory crosswalks are restricted, so they cannot contribute a table area
or a unit-level holdout. Their curves remain public but were not used in this
validation.

**BC geography is mixed for the coastal stratum.** The full benchmark contains
1,544 `bec_zone_fallback` visits; after the 40–150 age filter, the BC rows used
here contain 1,252 fallback visits
(6.9% of usable visits), dominated by Haida
Gwaii. That is a coarse default rather than a TSA-dominant assignment. The
validated coastal factor is therefore a coastal-region level factor, not a
clean southern-coast factor. The `fallback_share` column in
`correction_validation.csv` reports the mix for every stratum.

**BC single-TSA strata cannot be validated.** Boreal Foothills, Hay-Slave
Lowlands and Southern Boreal Cordillera each contain one TSA. A whole-TSA
holdout leaves no training or no test data; they are `insufficient_support`
regardless of their fit diagnostics.

**This is volume only.** No AGB, height, taper, grade, MAI or rotation-age
claim is made. The benchmark is a curve-level comparison, not a stand-level
inventory audit.
