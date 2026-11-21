# Deprecated: old v2d net-value layer (superseded)

**Status:** deprecated on 2026-11-21. Retained for audit only. Do not cite these
files as a net value.

This directory was built from the earlier `net_value_benchmark/` artifact and
the old workflow `workflows/national/harvest/net_value_v2d.py`. It:

- framed the QC T2/T20 difference as a benchmark and carried monetary
  `net_value_before/after_transfers` columns;
- included a QC reference built from the deprecated QC artifact rather than the
  corrected procurement benchmark;
- did not include a separate BMMB reference file.

The corrected replacement layer is:

```text
data/derived/national/harvest_basis/forest_economics_v2d/
```

with:

- `net_value_status=not_estimated` on every summary row;
- `policy_grade=false` on every summary row;
- `net_value_is_combined_national=false` on every summary row;
- QC procurement cost spreads copied and validated from
  `procurement_benchmark/`, never presented as revenue;
- no BC partial net value and no combined QC+BC monetary total.

Replacement planning note: `planning/net-value-v2d.md` (corrected banner).

Replacement builder: `workflows/national/harvest/forest_economics_v2d.py`.

Do not delete these old files; they are kept only so earlier reviews and
commits remain traceable.
