# OSeCAN availability and reduced biomass-module analysis

Status: **FRESH-side provisional**. This is not an official C2070
result. The model was run from the public `deltae/C2070` repository;
the reduced analysis uses the documented OSeCAN v0.3 placeholders.

## 1. Availability

| Item | Result |
|---|---|
| PyPI `osecan` JSON | HTTP 404 (not published) |
| `pip index versions osecan` | `ERROR: No matching distribution found for osecan` |
| `pip download/install osecan` | `ERROR: No matching distribution found for osecan` |
| `github.com/deltae/C2070` | public, HEAD `40d5b43bb3f8` |
| `github.com/eliasinul/CLEWsCAN2070` | public, redirects to `deltae/C2070` |
| `github.com/UBC-FRESH/CLEWsCAN2070` | 404 |
| C2070 site | `/site/model.html`, `/site/api.html`, `/site/data.html` all HTTP 200 |
| Install | `uv sync --frozen` succeeded with uv 0.13.9, Python 3.12 |
| Solver | GLPK via swiglpk 5.0.13; no Gurobi licence needed |

The documented install is `git clone https://github.com/eliasinul/CLEWsCAN2070.git`
then `uv sync`. The package is a `uv` project, not a PyPI wheel.
The site documents the same command sequence that was run.

## 2. Model run

Scenario: **Current Measures**. Horizon 2021-2070, single `REGION=CAN`,
13 fixed-width zones. The sequence was:

```bash
uv sync --frozen
uv run python -m osecan.cli build-sets
uv run python -m osecan.cli build-params
uv run python -m osecan.cli retrieve
uv run python -m osecan.cli clean-demand "Current Measures"
uv run python -m osecan.cli harmonize
python -m osecan.pipeline.assemble --out results/base/input
otoole convert csv datafile results/base/input results/base/osecan.txt config/otoole.yaml
python -m osecan.pipeline.solve --run results/base
python -m osecan.cli report --run results/base --out /tmp/osecan_report.html
```

The site's seven-command summary omits `assemble` and `otoole convert`;
both are required to turn the CSV parameter set into `results/base/osecan.txt`.
`solve` preprocesses the datafile and runs GLPK through `swiglpk`;
`report` produced an 851 KB HTML dashboard. `clean-demand` produced
9,328 PJ of 2025 national end-use demand, matching the model README's
9,328 PJ. Runs were executed in a temporary clone at `/tmp/osecan_src`;
only the summaries are retained in this repository.

The baseline and BC-base runs are both optimal:

| Run | Status | Objective (M$ discounted) | LP size |
|---|---|---:|---|
| Baseline 50 PJ/$4 placeholder | optimal | 1,331,287.25 | 273,001 x 234,900 |
| BC base national rollup | optimal | 1,331,287.25 | 273,001 x 234,900 |
| Hydro-frozen base diagnostic | optimal | 1,346,217.65 | 273,651 x 234,900 |
| Hydro-frozen high diagnostic | optimal | 1,346,217.65 | 273,651 x 234,900 |

The baseline and BC-base objectives are identical to the cent. That is
the first signal that the BC supply parameters do not enter the solution.
The BC-base datafile was verified before assembly: SUPBCW cap is
50.473 PJ in 2021 and 42.959 PJ in 2028-2070, and variable cost is
2.456978 $/GJ. The zero dispatch is an economic result, not a failed
file substitution.

### SUPBCW activity

The model has no `SUPBCWB1` or `SUPBCWB2` technology. Its only BC woody
residue supply code is the national `SUPBCW`. Activity is zero in every
year and every run:

| Run | 2021 | 2025 | 2030 | 2050 | 2070 | Total |
|---|---:|---:|---:|---:|---:|---:|
| baseline_placeholder | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| bc_base_national_rollup | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| diag_hydro_frozen_base | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| diag_hydro_frozen_high | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

`SUPBSW`, `PWRBCW`, and `PWRBIO` are also zero in every run.
The model meets electricity demand from hydro in the base runs and
from gas in the hydro-frozen diagnostics.

### Emissions and dispatch

| Run | 2025 (Mt CO2) | 2030 (Mt CO2) | 2050 (Mt CO2) | 2050 generation |
|---|---:|---:|---:|---|
| baseline_placeholder | 0.000 | 1.031 | 1.031 | HYD 3,231.9 PJ, NGS 20.2 PJ |
| bc_base_national_rollup | 0.000 | 1.031 | 1.031 | HYD 3,231.9 PJ, NGS 20.2 PJ |
| diag_hydro_frozen_base | 1.814 | 9.337 | 52.103 | HYD 2,230.5 PJ, NGS 1,021.6 PJ |
| diag_hydro_frozen_high | 1.814 | 9.337 | 52.103 | HYD 2,230.5 PJ, NGS 1,021.6 PJ |

The base model is a hydro-expansion model: 2050 hydro generation is
3,231.95 PJ and gas is 20.22 PJ. The hydro-frozen diagnostic is a
sensitivity probe that removes the unconstrained-hydro dominance;
gas fills the gap and biomass still does not dispatch.

### Zonal-file compatibility

The zonal files were tested directly:

```text
[FAIL] TotalTechnologyAnnualActivityUpperLimit.csv
        - TECHNOLOGY not in SETS: ['SUPBCWB1', 'SUPBCWB2']
[FAIL] VariableCost.csv
        - TECHNOLOGY not in SETS: ['SUPBCWB1', 'SUPBCWB2']
6 harmonization issue(s) found.
```

`PWRBCWB1` and `PWRBCWB2` exist, but they consume the national `BCW`
fuel. There is no `SUPBCWB1/B2` supply technology and no `BCWB1/BCWB2`
fuel. Loading the zonal files would require a model-structure change,
not a parameter substitution. The BC base run therefore uses the
national `comparison/SUPBCW_*` rollup, which is exactly B1+B2.
B1 and B2 have identical costs in every case and feed the same national
BCW pool, so adding separate zonal supply technologies would change the
reported split, not the aggregate BCW use or the cap-binding conclusion.

## 3. Reduced biomass-module economics

### Plant parameters

| Plant | Fuel | IAR | Efficiency | Capex ($/kW) | Fixed ($/kW-yr) | Var ($/GJ) | Life (yr) | CF | CO2 (t/GJ) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PWRBCW | BCW | 3.72 | 26.9% | 3,200 | 95 | 0 | 30 | 0.70 | 0 |
| PWRBIO | BIO | 2.85 | 35.1% | 3,000 | 90 | 2.5 | 30 | 0.70 | 0 |
| PWRBSW | BSW | 3.72 | 26.9% | 3,200 | 95 | 0 | 30 | 0.70 | 0 |
| PWRNGS | NGS | 2.70 | 37.0% | 1,100 | 25 | 3.0 | 30 | 0.85 | 0.051 |
| PWRHYD | HYD | 1.00 | 100% | 3,500 | 40 | 0 | 60 | 0.45 | 0 |

The exact PWRBCW input activity ratio 3.72 gives 26.88% efficiency;
the table rounds it to the documented 26.9%.

### LCOE (2020 CAD/MWh, 5% discount)

| Plant | Case | Fuel ($/GJ) | Carbon ($/t) | Capital+fixed | Fuel | Carbon | Var O&M | LCOE |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| PWRBCW | low | 3.194 | 0 | 49.44 | 42.77 | 0.00 | 0.00 | **92.21** |
| PWRBCW | base | 2.457 | 0 | 49.44 | 32.90 | 0.00 | 0.00 | **82.34** |
| PWRBCW | high | 1.966 | 0 | 49.44 | 26.32 | 0.00 | 0.00 | **75.76** |
| PWRBCW | placeholder | 4.000 | 0 | 49.44 | 53.57 | 0.00 | 0.00 | **103.01** |
| PWRBIO | generic | 3.000 | 0 | 46.50 | 30.78 | 0.00 | 9.00 | **86.28** |
| PWRBSW | placeholder | 4.000 | 0 | 49.44 | 53.57 | 0.00 | 0.00 | **103.01** |
| PWRNGS | carbon_2026 | 3.000 | 95 | 12.97 | 29.16 | 17.44 | 10.80 | **70.37** |
| PWRNGS | carbon_2030 | 3.000 | 115 | 12.97 | 29.16 | 21.11 | 10.80 | **74.04** |
| PWRHYD | generic | 0.000 | 0 | 57.05 | 0.00 | 0.00 | 0.00 | **57.05** |

The PWRBCW low/base/high LCOEs are **92.21**, **82.34**, and **75.76 $/MWh**.
Generic BIO is 86.28 $/MWh.
The model's gas plant is 70.37 $/MWh
at $95/t and 74.04 $/MWh at $115/t.
Hydro is 57.05 $/MWh.

### BCW versus generic BIO and gas

| Case | BCW $/GJ | BCW fuel $/MWh | BCW LCOE | BIO LCOE | Delta vs BIO | Breakeven vs BIO | Delta vs gas $95 | Delta vs gas $115 | Carbon parity vs gas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| low | 3.194 | 42.77 | 92.21 | 86.28 | 5.93 | 2.751 | 21.85 | 18.17 | 214.0 |
| base | 2.457 | 32.90 | 82.34 | 86.28 | -3.94 | 2.751 | 11.97 | 8.30 | 160.2 |
| high | 1.966 | 26.32 | 75.76 | 86.28 | -10.52 | 2.751 | 5.39 | 1.72 | 124.4 |

The per-MWh feedstock costs are:

- PWRBCW base: 3.6 x 3.72 x 2.457 = **32.90 $/MWh**.
- PWRBIO: 3.6 x 2.85 x 3.00 = **30.78 $/MWh**.
- Break-even BCW price against generic BIO: **2.751 $/GJ**.

The base and high cases beat generic BIO (base by 3.94 $/MWh, high by 10.52 $/MWh).
The low case loses to BIO. All three cases lose to the model's gas
plant at the documented $95-115/t carbon schedule.

### Cap metrics

| Case | 2021 cap (PJ) | 2028 cap (PJ) | Max electricity 2021 (PJ) | Max electricity 2028 (PJ) | Max electricity 2028 (TWh) |
|---|---:|---:|---:|---:|---:|
| low | 30.193 | 25.690 | 8.117 | 6.906 | 1.918 |
| base | 50.473 | 42.959 | 13.568 | 11.548 | 3.208 |
| high | 64.700 | 55.050 | 17.393 | 14.798 | 4.111 |

The 50 PJ placeholder is 13.441 PJ
of electricity (3.734 TWh).
The base 2028 cap is 11.548 PJ
(3.208 TWh), or
0.51% of the model's
2025 hydro generation. The cap is small relative to the power
system; the binding constraint is economics, not the cap.

The 50 PJ placeholder is applied per SUP technology in
`build_params.py`: `SUPBCW` and `SUPBSW` each get 50 PJ, so the
combined placeholder feedstock cap is 100 PJ, not 50 PJ. There is no
combined biomass feedstock cap.

### Does the cap bind?

**No** in every baseline and diagnostic run: `SUPBCW` activity is zero.
The cap is an upper bound that is never approached. The reasons are:

1. In the base model, unconstrained hydro is 57.05 $/MWh,
   below PWRBCW low/base/high (92.21 /
   82.34 /
   75.76 $/MWh). Hydro expands to meet demand.
2. When hydro is frozen at 2021 activity as a diagnostic, the model's
   gas plant is 70.37-74.04 $/MWh;
   even the high BCW case is above the $115/t gas LCOE.
3. The break-even BCW prices are **1.563 $/GJ** at $95/t and **1.837 $/GJ** at $115/t.
   The base case is $2.457/GJ; the high case is $1.966/GJ. Both are above
   the $115/t break-even.
4. Carbon-price parity with gas is reached at **124.4 $/t** for the high case, **160.2 $/t** for the base case, and **214.0 $/t** for the low case.
   The model's schedule is $95/t in 2026 and $115/t in 2030, so none
   of the cases reach parity.

### Generic-BIO bypass

The cap constrains `SUPBCW`, not biomass electricity. `PWRBIO` consumes
`BIO` from the uncapped `RNWBIO` supply at $3/GJ. If biomass power were
economic, the model could meet any biomass electricity target with
`PWRBIO` after the BCW cap is exhausted. The BCW cap would only shift
feedstock from BCW to generic BIO; it would not cap biomass generation.
In the current runs the bypass is latent because PWRBIO is also above
the gas LCOE (86.28 vs
74.04 $/MWh at $115/t).

## 4. Policy sensitivity

Two forcing cases were run on 2026-11-17 in a disposable copy of the
public model at `/tmp/osecan_sens`; the public clone was not modified.
Both use the BC-base national rollup (42.959 PJ cap from 2028,
2.456978 $/GJ). The only model change is the CO2 penalty function, plus
the hydro upper limits in the second case.

| Run | Forcing | Status | Objective (M$) | SUPBCW total (PJ) | PWRBCW total (PJ) | Cap binds | Emissions total (Mt) |
|---|---|---|---:|---:|---:|---|---:|
| BC base | documented 95-115 $/t | optimal | 1,331,287.25 | 0.000 | 0.000 | no | 25.750 |
| carbon_200 | BC base with a $200/t CO2 penalty from 2026 | optimal | 1,331,527.92 | 0.000 | 0.000 | no | 1.857 |
| carbon_200_hydro_frozen | BC base with $200/t CO2 and hydro frozen at 2021 activity | optimal | 1,371,553.35 | 2,104.981 | 565.855 | yes | 43.991 |

`SUPBSW` and `PWRBIO` are zero in both sensitivity runs.

### SUPBCW activity by year (PJ)

| Run | 2021 | 2025 | 2030 | 2050 | 2070 | Total |
|---|---:|---:|---:|---:|---:|---:|
| carbon_200 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| carbon_200_hydro_frozen | 0.000 | 42.959 | 42.959 | 42.959 | 42.959 | 2,104.981 |

### PWRBCW electricity by year (PJ)

| Run | 2021 | 2025 | 2030 | 2050 | 2070 | Total |
|---|---:|---:|---:|---:|---:|---:|
| carbon_200 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| carbon_200_hydro_frozen | 0.000 | 11.548 | 11.548 | 11.548 | 11.548 | 565.855 |

At $200/t without a hydro constraint, biomass stays at zero: hydro
expands to 3,252 PJ in 2050 and the objective rises by only 240.67 M$
while cumulative emissions fall to 1.86 Mt. The carbon price changes
the merit order against gas, but not against hydro.

With $200/t and hydro frozen at 2021 activity, SUPBCW reaches
42.959 PJ in every year from 2022 and the cap binds from 2028 through
2070 (100.0% utilisation). PWRBCW produces 11.548 PJ/yr of electricity
(3.21 TWh), or 0.35% of 2050 generation. Wind supplies 977.3 PJ in
2050, gas 32.7 PJ, and PWRBIO remains zero. The objective rises by
40,266.10 M$.

These dispatch comparisons use the model's costs, not the reduced
LCOE table. The model charges the $3/GJ `RNW` resource placeholder,
so hydro is about 67.85 $/MWh and wind about 86.03 $/MWh; the
reduced table's 57.05 $/MWh hydro figure excludes that placeholder.
Wind is only 0.25 $/MWh below generic BIO, which is why PWRBIO is
just behind wind rather than far behind it.

### Conditions for BCW dispatch

- The CO2 price must exceed the BCW-vs-gas parity price: about 160 $/t for the base case, 124 $/t for the high case, and 214 $/t for the low case.
- A cheaper clean firm resource must be constrained. With unconstrained hydro, even $200/t leaves BCW at zero because hydro expands to 3,252 PJ in 2050.
- With $200/t and hydro frozen at 2021 activity, SUPBCW reaches the 42.959 PJ cap and PWRBCW produces 11.548 PJ/yr of electricity.

The cap that binds is the national `SUPBCW` cap. The model has no
zonal BC supply technology, so a zonal cap cannot be tested here.

The documented 95-115 $/t schedule is below the base-case parity
price of about 160 $/t even with hydro frozen, which is why the
earlier hydro-frozen diagnostic also had zero BCW.

### Sensitivity limitations

- The model has a national SUPBCW cap only. Zonal BC caps (SUPBCWB1/B2) cannot be represented without a model-structure change.
- BCW is a national fuel. In the hydro-frozen run PWRBCW dispatches in A1/A2/S1/Q1/Q2/T1/L1, not in B1/B2; the model does not allocate BC residue to BC.
- PWRBIO stays at zero in both sensitivity runs because the model's wind cost (about 86.03 $/MWh including the $3/GJ RNW resource placeholder) is marginally below generic BIO (86.28 $/MWh); the generic-BIO bypass is latent, not active.

Reproduction (disposable copy; the public clone is unchanged):

```bash
cd /tmp/osecan_sens
# build_params.py: return 95.0 if y < 2026 else 200.0
.venv/bin/python -m osecan.cli build-params --out data/params
.venv/bin/python -m osecan.cli clean-demand "Current Measures"
.venv/bin/python apply_bc_base.py
.venv/bin/python -m osecan.pipeline.assemble --out results/<run>/input
.venv/bin/otoole convert csv datafile results/<run>/input results/<run>/osecan.txt config/otoole.yaml
.venv/bin/python -m osecan.pipeline.solve --run results/<run>
```

For the hydro-frozen case, append the 650 `PWRHYD<zone>` rows from
`results/diag_hydro_frozen/input/TotalTechnologyAnnualActivityUpperLimit.csv`
to the assembled input before `otoole convert`.

## 5. Assumptions and limitations

- LCOE is a simplified busbar calculation. It excludes transmission,
  backup, balancing, and financing outside the 5% discount rate.
- PWRBCW and PWRBIO use the documented v0.3 input activity ratios and
  placeholder costs. They are not Canadian fleet averages.
- The gas comparator is the model's placeholder plant (capex 1,100 $/kW,
  fuel $3/GJ, CO2 0.051 t/GJ, carbon $95-115/t). A market gas price or
  a different capex would move the break-even.
- The BC zonal caps are FRESH-side provisional and not a C2070 boundary.
- The hydro-frozen diagnostic is a sensitivity probe, not a scenario.
- The model has no `SUPBCWB1/B2`; the BC base run is the national
  `SUPBCW` rollup. Zonal dispatch cannot be reported from this model.
- The model's `TotalDiscountedCost.csv` extraction is empty in this
  version; the objective is read from the GLPK solution instead.

## 6. Verification

- Four original OSeCAN solves returned `optimal` (two base, two diagnostics).
- The BC-base control replication and both policy sensitivity solves
  returned `optimal`; the control reproduced 1,331,287.25 M$.
- The zonal `harmonize` probe returned exit 1 with the expected
  `TECHNOLOGY not in SETS` errors.
- The reduced analysis is re-built by
  `python -m workflows.national.clews.osecan_biomass_module`.
- The focused test suite is
  `python -m pytest -q workflows/national/clews/tests/test_osecan_biomass_module.py`.

## 7. Gaps and next steps

1. Add `SUPBCWB1/B2` (and `BCWB1/B2` fuels) to `model_structure.py` if
   zonal BC supply constraints are required. The current model cannot
   represent them.
2. Add a hydro resource constraint or a provincial policy that makes
   biomass compete. The $200/t sensitivity shows that the carbon price
   alone is not enough while hydro is unconstrained; with hydro frozen,
   BCW reaches the 42.959 PJ cap at $200/t.
3. Replace the generic `RNWBIO` $3/GJ uncapped supply with a WS3/FABLE
   biomass supply curve, or add a biomass-wide cap. Otherwise the BCW
   cap is bypassed by generic BIO.
4. Replace the placeholder gas capex/fuel/carbon assumptions with
   Canadian values before drawing policy conclusions from the merit
   order.
5. Re-run the model after those changes; this report's run evidence is
   for the public v0.3 placeholder model only.

Generated: 2026-11-17T19:50:47+00:00
