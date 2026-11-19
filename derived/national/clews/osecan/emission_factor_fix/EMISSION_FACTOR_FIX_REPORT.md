# OSeCAN emission-factor unit fix and core national reruns

**Status:** FRESH-side provisional; not an official C2070 result.  
**Model copy:** `/tmp/osecan_emfix`, copied from `/tmp/osecan_supply_curve`; the public `deltae/C2070` repository was not modified.  
**Artifact:** `data/derived/national/clews/osecan/emission_factor_fix/`.

## 1. Fix diff and unit check

`src/osecan/data/build_params.py` wrote `ARCH[...]["co2"]` directly into
`EmissionActivityRatio` and into the UDC emission-cap multiplier. The OSeMOSYS
emissions equations (`E4`, `E5`, `E8`, `E9` in
`resources/osemosys_fast_osecan.txt`) apply `EmissionActivityRatio` to
`RateOfActivity`, which is output activity (PJ of electricity for `PWR*` plants).
The placeholder factors `0.051` and `0.090` are fuel-input factors in t/GJ,
numerically Mt/PJ of fuel. Each plant consumes `InputActivityRatio` PJ of fuel per
PJ of output, so the parameter must be scaled by that ratio.

Changed code (full patch in `emission_factor_fix.patch`):

```python
def emission_factor_per_output_pj(arch: str) -> float:
    input_ratio = float(ms.PowerPlants[arch][1])
    return round(float(ARCH[arch]["co2"]) * input_ratio, 6)
```

* `EmissionActivityRatio`: `attr["co2"]` -> `emission_factor_per_output_pj(a)`.
* `UDCMultiplierActivity` for emission caps: same scaling.
* Gas `NGS`: `0.051 × 2.70 = 0.1377` Mt/PJ output.
* Coal `COA`: `0.090 × 2.90 = 0.261` Mt/PJ output.
* 1,300 CSV rows changed (13 zones × 2 archetypes × 50 years); no UDC policies
  are active in the national scenarios, so the UDC path is unit-corrected but not
  exercised by these runs.

Unit check (`unit_check.json`):

| Plant | Test output (PJ) | Fuel input (PJ) | Fuel-basis emissions (Mt) | Corrected EAR × output (Mt) | Match |
|---|---:|---:|---:|---:|---|
| Gas `NGS` | 10 | 27.0 | 27.0 × 0.051 = 1.377 | 10 × 0.1377 = 1.377 | yes |
| Coal `COA` | 10 | 29.0 | 29.0 × 0.090 = 2.610 | 10 × 0.261 = 2.610 | yes |

No negative factors. For the solved baseline, reconstructing emissions from
`ProductionByTechnologyAnnual × corrected EAR` matches `AnnualEmissions.csv` to
`4.77e-7` Mt/year (CSV rounding). Only four gas technologies emit:
`PWRNGSN1`, `PWRNGSQ1`, `PWRNGSQ2`, `PWRNGST1`; no coal emits. No double
counting: the raw fuel-basis factor is no longer written anywhere in the
parameter set.

## 2. 119M baseline

`$95/t` to 2025, `$115/t` from 2026, normal hydro, 119M base cap, `SUPBCW`
carries rest-of-Canada and `SUPBCWT1..T4` are capped at zero.

| Metric | Pre-fix | Post-fix | Delta |
|---|---:|---:|---:|
| Objective (M$) | 1,331,289.52 | 1,331,575.72 | +286.20 |
| Emissions, 2021-2070 (Mt) | 25.714753 | 0.484962 | -25.229791 |
| Emissions, 2050 (Mt) | 1.0309 | 0.0 | -1.0309 |
| National BCW supply (PJ) | 0 | 0 | 0 |
| `PWRBCW` output (PJ) | 0 | 0 | 0 |
| `PWRHYD` 2050 (PJ) | 3,232.0 | 3,252.2 | +20.2 |
| Gas generation 2050 (PJ) | 20.2 | 0 | -20.2 |

The corrected baseline abates the ~504 PJ of gas generation that the pre-fix
baseline used over the horizon. Residual 0.485 Mt is gas in 2022 and 2024 only,
before the 2026 carbon-price step. No supply cap binds; BC zonal supply is zero
because hydro is cheaper.

## 3. 119M stress ($200/t, hydro upper cap at 2021)

| Metric | Pre-fix | Post-fix | Delta |
|---|---:|---:|---:|
| Objective (M$) | 1,371,124.38 | 1,371,773.42 | +649.04 |
| Emissions (Mt) | 38.544682 | 0.460752 | -38.083930 |
| National BCW supply (PJ) | 7,086.539 | 7,172.088 | +85.549 |
| BC zonal supply B1+B2 (PJ) | 1,872.589 | 1,887.878 | +15.289 |
| `PWRBCW` output (PJ) | 1,904.984 | 1,927.981 | +22.997 |
| `PWRBCWB1` output (PJ) | 44.584 | 46.150 | +1.566 |
| `PWRBCWB2` output (PJ) | 458.800 | 461.344 | +2.544 |
| Other `PWRBCW` output (PJ) | 1,401.599 | 1,420.487 | +18.888 |

`SUPBCW`, `SUPBCWB1`, and `SUPBCWB2` all bind (`SUPBCW` from 2024 and
2027-2070; B1 from 2026-2070; B2 from 2031-2070). Hydro is held at 2,230.55 PJ
from 2026. Post-2026 gas is zero. Residual 0.461 Mt is 2022/2024 gas only.

## 4. Tiered supply-curve stress ($200/t, hydro cap)

`SUPBCWT1..T4` replace `SUPBCW`; `SUPBCW` is disabled; BC zonal B1/B2 are
unchanged.

| Metric | Pre-fix | Post-fix |
|---|---:|---:|
| Objective (M$) | 1,371,124.50 | 1,371,773.03 |
| Emissions (Mt) | 38.457287 | 0.460752 |
| National BCW supply (PJ) | 7,087.666 | 7,173.704 |
| `PWRBCW` output (PJ) | 1,905.287 | 1,928.415 |

Tier dispatch (PJ):

| Tier | Cumulative 2021-2070 | 2050 | Cap 2050 | Binding |
|---|---:|---:|---:|---|
| `SUPBCWT1` | 4,107.367 | 85.0071 | 85.0071 | yes |
| `SUPBCWT2` | 1,178.461 | 24.3917 | 24.3917 | yes |
| `SUPBCWT3` | 0 | 0 | 39.8737 | no |
| `SUPBCWT4` | 0 | 0 | 64.2655 | no |

T1+T2 exactly equal the 119M rest-of-Canada cap (109.398863 PJ), so the tiered
$200 case reproduces the 119M base stress within 0.39 M$ and identical
emissions. T3/T4 remain dormant; the corrected carbon price does not pull the
high-cost tiers in.

## 5. $250, $300, and mandate

| Case | Objective (M$) | Emissions (Mt) | National BCW (PJ) | PWRBCW (PJ) | Binding tiers |
|---|---:|---:|---:|---:|---|
| $200 tiered | 1,371,773.03 | 0.460752 | 7,173.704 | 1,928.415 | T1, T2 |
| $250 tiered | 1,371,773.13 | 0.450327 | 7,173.704 | 1,928.415 | T1, T2 |
| $300 tiered | 1,371,773.13 | 0.450327 | 7,173.704 | 1,928.415 | T1, T2 |

Pre-fix comparison: $250 was 1,371,648.82 M$ / 2.446648 Mt; $300 was
1,371,649.82 M$ / 2.445288 Mt. The corrected $250/$300 cases leave dispatch
unchanged; only the degenerate T1/T2 split shifts because both have the same
variable cost. The residual ~0.45 Mt is pre-2026 gas, which a 2026 price cannot
touch.

The BCW-cap-saturation mandate diagnostic was attempted
(`efix_mandate_saturation`) but the GLPK solve had not returned within the
timebox and was stopped without a status file. It is not reported as a result.
Resume command is in `manifest.json`.

## 6. Comparison and verdict

**Does the $250 switch disappear?** Yes. Pre-fix, raising the 2026 price from
$200 to $250 cut cumulative emissions from 38.457 Mt to 2.447 Mt (a 36.01 Mt
switch). Post-fix, the same step cuts 0.4608 Mt to 0.4503 Mt (0.0104 Mt), and
dispatch/objective are unchanged. The switch has moved to at or below $200:
post-fix $200 already has zero gas after 2026, and the $115 baseline has only a
0.01 PJ gas sliver in 2028 after 2026. The remaining emissions are 2022/2024
gas, structurally outside the post-2026 price.

**Does BCW dispatch change?** Yes, modestly. In the $200 stress, national BCW
supply rises from 7,086.5 to 7,172.1 PJ (+1.21%) and `PWRBCW` output from
1,905.0 to 1,928.0 PJ (+1.21%). The tier mix is unchanged: T1+T2 binding, T3/T4
zero. Baseline BCW remains zero because hydro is cheaper than BCW at $115/t.

## 7. Caveats

* This is a local patch in a disposable copy. The public OSeCAN repository was
  not modified and no public commit was made.
* `src/osecan/model_structure.py` still describes the factors as "Mt CO2 per PJ
  of activity"; that comment is part of the unit error and should be corrected
  upstream.
* The reduced LCOE helper in `workflows/national/clews/osecan_biomass_module.py`
  computes `carbon = 3.6 × emission_factor` without the plant `IAR`. Its
  docstring calls the factor "per GJ of technology activity", but the numeric
  values are fuel-combustion factors. The LCOE carbon line is therefore also
  output-basis and remains inconsistent with this fix; it should be corrected in
  a separate change.
* The $200/$250/$300 cases are scenario sensitivities, not forecasts. The
  hydro stress is an annual upper bound at 2021 activity, not fixed dispatch.
* The tiered curve is RSYC-only; T4 is a documented high-cost marginal tier.
* Pre-fix `national_150m`, `national_base_119m`, `national_supply_curve`, and
  `demand_sensitivity` numeric files are retained; their emissions and objective
  results are superseded by this artifact (see `SUPERSEDED.md` notes).
