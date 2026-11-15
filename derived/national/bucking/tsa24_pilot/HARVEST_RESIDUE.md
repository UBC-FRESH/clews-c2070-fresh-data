# TSA24 harvest-slash residue ledger

This note documents the AGB-based harvest-slash ledger for the TSA24
bucking pilot. It is a model-output comparison, not a delivered-fuel
offer and not a field residue audit.

## Method

```
harvest_residue_odt = agb_odt - merchantable_log_biomass_odt
merchantable_log_biomass_odt = sum(log_volume_m3 * basic_density_odt_m3)
```

AGB is the FEMIC BTC `biomass-live` bank `Biomass_Live_Above` value at
the managed AU and FAIB stand age matched by BEC + leading species ->
AU stratum -> FEMIC site-index class -> AU. The BTC biomass family is
reported in oven-dry tonnes per hectare; `Biomass_Live_Above` is stem
wood + bark + foliage + branch, with roots and total reported separately.

The stand-level AGB is applied to the plot on a per-hectare basis and
scaled by `observed_merchantable_all / BTC_volume` so AGB and the pilot
log volume share the same plot productivity basis. No per-tree AGB is
invented. Merchantable log biomass is expanded from the sampled trees by
`PHF_TREE` and then by the observed all-tree/sampled-tree merchantable
volume ratio.

## Coverage and screen

- Pilot plots: 20
- Primary ledger plots: 8
- Excluded plots: 12
- BTC volume AU matches: 14 of 20; positive-volume joins: 12

Plots are excluded from the primary ledger when there is no managed AU,
the BTC volume is zero at the plot age, the observed/BTC volume ratio is
outside the documented band, or AGB does not exceed log biomass. Excluded
plots remain in `harvest_residue_ledger.csv` with a status and reason.

## Basic density

Species-specific defaults are in
`workflows/national/bucking/rules/bc_basic_density.csv`. The values come
from the FVS-BC variant NBEL/FIA wood dry-weight table (Smith & Miles
2009), converted from dry lb/ft³ to ODT/m³ at 16.01846 kg/m³ per lb/ft³.
They are species defaults, **not** BC-local sampled values.

| Species | ODT/m³ |
| --- | --- |
| SW / S (white spruce) | 0.3598 |
| SB (black spruce) | 0.3798 |
| SE (Engelmann spruce) | 0.3298 |
| PL (lodgepole pine) | 0.3798 |
| FD (Douglas-fir) | 0.4498 |
| BL (subalpine fir) | 0.3098 |
| CW (western redcedar) | 0.3098 |
| HW (western hemlock) | 0.4198 |
| AT (trembling aspen) | 0.3498 |
| EP (paper birch) | 0.4798 |
| AC (black cottonwood) | 0.3098 |

## Recovery, moisture, and chip assumptions

- Roadside recovery factor: 60% of AGB-based slash.
- Moisture, green: 45% wet basis.
- Moisture, seasoned: 30% wet basis.
- Chip yield: 90% of green residue tonnes.

## Results (primary plots)

| Metric | Mean | Median | Min | Max |
| --- | --- | --- | --- | --- |
| AGB (ODT/ha) | 200.921 | 155.910 | 101.692 | 439.625 |
| Merchantable log biomass (ODT/ha) | 88.274 | 76.382 | 35.225 | 166.199 |
| Harvest slash (ODT/ha) | 112.648 | 83.351 | 57.858 | 277.538 |
| Harvest slash, unscaled AGB (ODT/ha) | 123.348 | 122.264 | 58.293 | 180.749 |
| Taper residue (ODT/ha) | 21.008 | 18.797 | 6.551 | 46.722 |
| Non-taper residue (ODT/ha) | 91.640 | 57.572 | 39.726 | 230.816 |
| Recoverable slash (ODT/ha) | 67.589 | 50.011 | 34.715 | 166.523 |
| Slash per m³ log (ODT/m³) | 0.483 | 0.403 | 0.325 | 0.778 |
| Taper residue per m³ taper total (ODT/m³) | 0.082 | 0.092 | 0.021 | 0.139 |

- Primary-plot hectares (each plot treated as one hectare): 8
- Harvest slash total: 901.183 ODT
- Taper residue total: 168.065 ODT
- Recoverable slash total: 540.710 ODT
- Recoverable green tonnes at 45%: 983.109 t
- Recoverable chip green tonnes at 45% and 0.90 yield: 884.798 t
- Harvest-to-taper residue ratio: 5.36

## Difference from taper residue and mill residue

AGB-based harvest slash is larger than the pilot taper residue because
AGB includes bark, branches, and foliage, while the taper ledger only
covers the stump-height section, top, and unmerchantable stem sections.
The per-plot ledger reports both quantities and the branch+foliage+bark
and unmerchantable-wood components.

BTC `Residual_Chips`, `Residual_Sawdust`, `Residual_Shavings`,
`Residual_Trim`, and `Residual_Bark` are **mill-processing residues**.
They are not harvest slash, are not on the same basis, and are deliberately
excluded from this ledger. No ratio against `Residual_*` is computed.

## Limitations

- AGB is a stand-level BTC model output at the managed AU site index, not a
  plot measurement.
- The FAIB stand age and the managed AU age origin are not guaranteed to be
  the same clock; the volume-ratio screen removes the worst mismatches but
  does not eliminate the join uncertainty.
- Basic density is a species default, not a BC-local sample.
- Recovery, moisture, and chip yield are assumptions.
- The sample is 20 plots / 300 trees; this is a pilot, not a TSA-wide
  residue supply estimate.
