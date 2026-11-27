# WS4-driven 119 Mm3 harvest and chain comparison

**Artifact:** `ws4_chain_119m` **Version:** 1.0.0

**Status:** pass. New sidecar artifact. The national WS4 dataset tables, frozen
chain v5.1, and official OSeCAN are unchanged.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`,
`official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Method

The national WS4 estate at 990-m fragments was read from
`data/derived/ws4/scanfi-national-990m/dataset/`. Each fragment belongs to a
natural/unmanaged track whose name carries `AU(<province>)`; the track's
`feature.Yield.<province>.unmanaged.Total` feature supplies the RSYC yield
curve. Fragment volume is `area_ha * curve(age)` at the exact integer age.
Block volume is the sum of its fragment volumes. No block volume is scaled or
fabricated.

Eligible blocks are natural/unmanaged blocks with `offset >= 40`. A
volume-aware greedy selects whole blocks in descending volume, fills while the
next block fits, then chooses the unselected block that minimises the absolute
overshoot. Provincial achieved volume can exceed the control target by at most
the final block volume. The same block is never selected twice. NU has a zero
control target and no schedule row.

The schedule has **45 rows** (`block_id,treatment,offset`) at
offset 0. `ws4 validate` returned `Dataset is valid → /srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/derived/ws4/scanfi-national-990m/dataset`. The one-year `CC`
simulation status is `reused`. Harvested volume and treated area are read
from `product.HarvestedVolume.<province>.unmanaged.CC` and
`product.Treated.<province>.unmanaged.CC`.

## 2. Achieved provincial harvest

| Province | Target (Mm3) | Achieved (Mm3) | Delta (m3) | Area (ha) | Blocks | Mean age | Curves |
|---|---|---|---|---|---|---|---|
| BC | 39.978577 | 39.978582 | 5.326 | 291643.47 | 8 | 83.75 | 7 |
| AB | 22.891404 | 22.891408 | 4.290 | 182523.78 | 4 | 94.35 | 4 |
| SK | 4.344698 | 4.344701 | 2.999 | 103128.75 | 3 | 45.86 | 3 |
| MB | 1.135236 | 1.135238 | 2.070 | 18734.04 | 3 | 63.74 | 3 |
| ON | 13.493596 | 13.493598 | 1.979 | 70730.37 | 4 | 72.41 | 4 |
| QC | 26.674334 | 26.674336 | 2.267 | 325022.04 | 4 | 122.68 | 4 |
| NB | 6.234700 | 6.234713 | 13.366 | 48731.22 | 5 | 61.85 | 5 |
| NS | 2.388245 | 2.388248 | 2.670 | 17590.59 | 4 | 73.72 | 4 |
| PE | 0.302210 | 0.302221 | 10.256 | 2304.90 | 3 | 56.17 | 3 |
| NL | 1.454038 | 1.454041 | 3.295 | 21849.03 | 3 | 94.99 | 3 |
| YT | 0.043926 | 0.043929 | 3.328 | 851.94 | 2 | 84.32 | 1 |
| NT | 0.036376 | 0.036378 | 1.933 | 628.92 | 2 | 64.13 | 2 |
| NU | 0.000000 | 0.000000 | 0.000 | 0.00 | 0 | 0.00 | 0 |

National target is **118.977339
Mm3** (the nominal 119 Mm3 control, whose exact provincial sum is
118.9773391 Mm3). National achieved harvest is
**118.977393 Mm3**; treated area is
**1,083,739.05 ha**.

## 3. Chain v5.1 coefficients and comparison

The frozen v5.1 per-province product/residue coefficients are the frozen
`product_chain_by_province.csv` outputs divided by the frozen provincial
harvest. The `ws4_achieved` basis applies them to the realised WS4 harvest.
The `scaled_to_119m_control` basis applies one national factor
`0.999999547984` to every province,
preserving WS4 provincial shares and matching the control total.

| Metric | Unit | v5.1 | WS4 achieved | WS4 delta | WS4 delta % | Scaled | Scaled delta | Scaled delta % |
|---|---|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 1.18977e+08 | 1.18977e+08 | 53.7797 | 0.0000 | 1.18977e+08 | 1.49012e-08 | 0.0000 |
| solid_product_m3 | m3 | 3.76736e+07 | 3.76736e+07 | 14.7015 | 0.0000 | 3.76736e+07 | -2.32758 | -0.0000 |
| sawlog_product_m3 | m3 | 3.3957e+07 | 3.3957e+07 | 13.2512 | 0.0000 | 3.3957e+07 | -2.09795 | -0.0000 |
| panel_product_m3 | m3 | 3.71664e+06 | 3.71664e+06 | 1.45036 | 0.0000 | 3.71664e+06 | -0.229624 | -0.0000 |
| pulp_product_odt | odt | 1.20663e+07 | 1.20663e+07 | 6.12512 | 0.0001 | 1.20663e+07 | 0.670948 | 0.0000 |
| pellet_product_odt | odt | 5.22969e+06 | 5.22969e+06 | 2.95324 | 0.0001 | 5.22969e+06 | 0.589341 | 0.0000 |
| bio_product_mwh | MWh | 930946 | 930947 | 0.525712 | 0.0001 | 930946 | 0.10491 | 0.0000 |
| process_residue_m3 | m3 | 5.991e+07 | 5.991e+07 | 26.8307 | 0.0000 | 5.991e+07 | -0.249574 | -0.0000 |
| process_residue_odt | odt | 2.69595e+07 | 2.69595e+07 | 12.0738 | 0.0000 | 2.69595e+07 | -0.112308 | -0.0000 |
| process_residue_pj | PJ | 498.751 | 498.751 | 0.000223366 | 0.0000 | 498.751 | -2.0777e-06 | -0.0000 |
| harvest_residue_gross_odt | odt | 2.40222e+07 | 2.40222e+07 | 12.4636 | 0.0001 | 2.40222e+07 | 1.60518 | 0.0000 |
| harvest_residue_gross_pj | PJ | 444.411 | 444.411 | 0.000230577 | 0.0001 | 444.411 | 2.96958e-05 | 0.0000 |
| harvest_residue_recoverable_r035_odt | odt | 8.40777e+06 | 8.40778e+06 | 4.36226 | 0.0001 | 8.40777e+06 | 0.561812 | 0.0000 |
| harvest_residue_recoverable_r035_pj | PJ | 155.544 | 155.544 | 8.07019e-05 | 0.0001 | 155.544 | 1.03935e-05 | 0.0000 |
| harvest_residue_recoverable_r060_odt | odt | 1.44133e+07 | 1.44133e+07 | 7.47816 | 0.0001 | 1.44133e+07 | 0.963106 | 0.0000 |
| harvest_residue_recoverable_r060_pj | PJ | 266.646 | 266.647 | 0.000138346 | 0.0001 | 266.646 | 1.78175e-05 | 0.0000 |
| harvest_residue_recoverable_r075_odt | odt | 1.80167e+07 | 1.80167e+07 | 9.3477 | 0.0001 | 1.80167e+07 | 1.20388 | 0.0000 |
| harvest_residue_recoverable_r075_pj | PJ | 333.308 | 333.308 | 0.000172933 | 0.0001 | 333.308 | 2.22718e-05 | 0.0000 |
| total_residue_gross_pj | PJ | 943.162 | 943.162 | 0.000453943 | 0.0000 | 943.162 | 2.76181e-05 | 0.0000 |
| total_residue_recoverable_r035_pj | PJ | 654.295 | 654.295 | 0.000304068 | 0.0000 | 654.295 | 8.31582e-06 | 0.0000 |
| total_residue_recoverable_r060_pj | PJ | 765.397 | 765.398 | 0.000361712 | 0.0000 | 765.397 | 1.57398e-05 | 0.0000 |
| total_residue_recoverable_r075_pj | PJ | 832.059 | 832.059 | 0.000396298 | 0.0000 | 832.059 | 2.01941e-05 | 0.0000 |

`solid_product_m3` is sawlog product plus panel product. PJ values use
18.5 GJ/ODT. Process residue and harvest residue are never summed into a single
stream; `total_residue_gross_pj` is reported only as the arithmetic national
total of the two separate streams.

## 4. Caveats

- The schedule is a whole-block arithmetic verification, not a sustainable
  harvest, AAC, policy result, or investment case.
- Blocks are selected whole. Provincial overshoot is block-granularity
  overshoot, not a scaled target.
- 990-m forest-area fragments and group yield curves are inventory
  realisations, not operable or tenure-feasible areas.
- One `CC` treatment at offset 0 is simulated. The managed track shares the
  natural curve; planting response, silviculture, fertilization, and genetic
  gain are not modelled.
- Facility assignment, mill capacity, transport, and interprovincial trade are
  not re-run. Products and residue are coefficient applications by origin
  province.
- The scaled basis is a national factor that preserves WS4 provincial shares;
  it is not per-province target scaling.
- 0.60 harvest recovery is a reference case, not a calibrated recovery factor.
- No official OSeCAN file or public OSeCAN surface is changed.

## 5. OSeCAN handoff status

Not rebuilt. The existing residue-curve and OSeCAN handoff workflows are frozen to the v5.1 facility assignment and zone-weight inputs; a WS4-basis rerun would require a facility assignment and province-to-zone reallocation outside this schedule scope. Only chain totals were rebuilt; no tier position is claimed.

## 6. Reproduce

```bash
.venv/bin/python -m workflows.national.facilities.ws4_chain_119m
```
