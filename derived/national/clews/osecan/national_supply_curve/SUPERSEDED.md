# Superseded for emissions and objective

This directory predates the OSeCAN emission-factor unit correction applied in
`../emission_factor_fix/`.

Emission totals, objectives, and any conclusions conditioned on them in this
directory are **superseded**. The numeric files are retained unchanged for audit
and reproducibility. Do not cite emissions or objective values from this
directory without the correction.

The correction multiplies the fuel-input emission factors by each plant's
InputActivityRatio before writing `EmissionActivityRatio` (gas 0.051 -> 0.1377,
coal 0.090 -> 0.261 Mt/PJ output). See
`../emission_factor_fix/EMISSION_FACTOR_FIX_REPORT.md` and `../emission_factor_fix/emission_factor_fix.patch`.

Superseded: 2026-11-19.
