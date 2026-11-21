# Deprecated: QC net-value benchmark (superseded)

**Status:** deprecated on 2026-11-21. Retained for audit only. Do not cite the
QC “residual” as forest net value.

The files in this directory frame `T2 purchase - T20 BGAD` as a pre-Crown
“residual” or forest-sector net value. That framing is wrong:

- Table 2 (`107.22`) is a **buyer-side procurement cost** covering purchase,
  State transfers, transport/unloading, and road costs where applicable. It is
  not observed log-sale revenue.
- Table 20 (`81.40` before, `25.01` transfers, `106.41` after) is the **BGAD
  procurement cost** for a different respondent sample. It excludes species
  gain/loss, and PRCCM road rebates sit inside transfers.
- `107.22 - 81.40 = 25.82` and `107.22 - 106.41 = 0.81` are therefore
  **procurement-channel cost spreads**, not forest net value.
- The old QC/M CAD volume sensitivity must not be used. It multiplied a cost
  spread by a screening allocation volume and produced a misleading “net value”.

The replacement artifact is:

```text
data/derived/national/harvest_basis/procurement_benchmark/
```

with:

- `net_value_status=not_estimated`
- `interpretation=purchased_vs_bgad_procurement_cost_spread`
- `policy_grade=false`
- no QC or M CAD net-value sensitivity.

Replacement planning note: `planning/procurement-benchmark.md`.

Replacement builder: `workflows/national/harvest/procurement_benchmark_v1.py`.

Do not delete these old files; they are kept only so earlier reviews and
commits remain traceable.
