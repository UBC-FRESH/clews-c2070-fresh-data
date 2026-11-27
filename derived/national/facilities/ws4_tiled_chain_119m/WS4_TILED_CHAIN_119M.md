# Tiled 30-m WS4 119 Mm3 chain

**Artifact:** `ws4_tiled_chain_119m` **Version:** 1.0.0

**Status:** pass. The 3,345 built and validated tiled WS4 datasets were
scanned. Frozen chain v5.1, the national 990-m dataset, the tiled datasets and
official OSeCAN are unchanged.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `tiled_30m=true`,
`official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Coverage

- Candidates in the upstream manifest: **3562**
- Built and validated tile datasets scanned: **3345**
- Explicit zero-harvest skips: **203**
- Explicit no-forest skips: **14**
- Provinces with tile datasets: AB, BC, MB, NB, NL, NS, NT, ON, PE, QC, SK, YT
- Provinces without tile datasets: NU

This is full coverage of the built+validated tiled estate, not a fabricated
dataset for the 217 explicitly skipped candidates. NU has a zero control target
and all 203 NU candidates were skipped upstream as zero-harvest, so no NU
dataset exists to scan.

## 1b. THIN refresh

| Refresh field | Value |
|---|---|
| Coverage manifest SHA-256 | 2f2d55a2f30eaf185c2ab50a9260a6bf2f092070cbad4eeb2b97242b003e1509 |
| Prior coverage manifest SHA-256 | bb1f831b7ba5814d68d457f496a72bddc9e342aa49e50730858d8a8d5ba418eb |
| THIN propagated | true |
| THIN tiles | 3345 |
| THIN tracks excluded from selection | 12892 |
| CC contracts unchanged | true |
| CC contract tiles | 3345 |
| CC contract tree SHA-256 | 1d03d98888483f90a499e1b8673ec5c4fa677bcd1701a3360ed2392ce2910af4 |
| Full rescan / cache | full_rescan |
| Pre-THIN results unchanged | True |
| Comparison rows / mismatches | 223 / 0 |
| Max absolute delta | 1.4901161193847656e-08 |
| Rerun UTC | 2026-11-27T07:11:54+00:00 |

The coverage was refreshed from the metadata-only THIN-patched national tiled
manifest. Every tile's per-tile `thin_patch.json` records an identical
natural/managed CC contract hash before and after the patch, and the parser
explicitly excludes `SILV_STATE(thinned)` tracks from the natural/unmanaged
candidate pool. The refreshed scan is compared row-for-row with the pre-THIN
artifact in `thin_refresh_comparison.csv`. `pre_thin_results_unchanged=true`
means selection keys, selected area, harvest, chain totals and OSeCAN tier
positions all match exactly; any difference is written to that CSV with its
signed delta.

## 2. Two-pass method

**Pass 1 - candidate scan.** For each tile, only `blocks`, `tracks`,
`features` and `curves` are read. Natural/unmanaged tracks are parsed from
`AU(<tile id>)+IFM(unmanaged)+ORIGIN(natural)`; the province is taken from the
tile slug/manifest and the AU code is checked against the tile id. Each natural
track is joined to its `feature.Yield.*.unmanaged.Total` curve. Block
approximate volume is `area_ha * curve(block offset)`. Blocks with
`offset >= 40` and positive approximate volume are ranked; the top
20,000 per tile are written to a candidate Parquet. The
per-province pool is the top 2,000,000 of those candidates by
approximate volume (or all candidates when smaller), and must exceed the
provincial target by at least 10%.

**Selection.** Whole blocks are selected by a volume-aware greedy in
descending approximate volume. The greedy fills while the next block fits and
then picks the unselected block that minimises overshoot. No block is selected
twice.

**Pass 2 - exact volume.** For the largest
50,000 provincial candidates by approximate volume (and
further 50,000-block batches if needed), `fragments` are read and block volume
is `sum(fragment area * curve(fragment age))` at the exact integer fragment
age. Fragment area must equal block area within 1e-06 ha and
every fragment must belong to the block's natural track. After exact volumes
are known, the greedy is re-run on exact volumes so the final schedule is a
whole-block subset close to the provincial target.

## 3. Exact harvest by province

| Province | Target Mm3 | Exact Mm3 | Delta m3 | Area ha | Blocks | Tiles | Mean age | Exact/approx |
|---|---|---|---|---|---|---|---|---|
| BC | 39.978577 | 39.979843 | 1266.312 | 255377.2 | 29 | 26 | 53.57 | 1.035342 |
| AB | 22.891404 | 22.893881 | 2477.065 | 212312.8 | 11 | 10 | 43.94 | 1.061935 |
| SK | 4.344698 | 4.345555 | 857.476 | 64281.0 | 6 | 6 | 56.67 | 1.039005 |
| MB | 1.135236 | 1.135894 | 657.881 | 9264.1 | 3 | 3 | 104.33 | 1.010946 |
| ON | 13.493596 | 13.494425 | 828.572 | 67809.1 | 5 | 5 | 86.17 | 1.009090 |
| QC | 26.674334 | 26.676208 | 1873.514 | 362592.8 | 22 | 20 | 92.06 | 1.016830 |
| NB | 6.234700 | 6.235446 | 746.141 | 35912.3 | 240 | 31 | 62.71 | 1.031574 |
| NS | 2.388245 | 2.388791 | 546.054 | 23190.5 | 9 | 8 | 84.98 | 1.012224 |
| PE | 0.302210 | 0.302285 | 74.484 | 2124.9 | 93 | 9 | 72.55 | 1.024781 |
| NL | 1.454038 | 1.454944 | 906.059 | 29808.5 | 5 | 4 | 63.09 | 1.004871 |
| YT | 0.043926 | 0.044371 | 445.636 | 294.6 | 2 | 2 | 48.40 | 1.047636 |
| NT | 0.036376 | 0.037228 | 852.302 | 141.2 | 2 | 2 | 107.57 | 1.003608 |
| NU | 0.000000 | 0.000000 | 0.000 | 0.0 | 0 | 0 | 0.00 | 0.000000 |

National target is **118.977339 Mm3**;
national exact harvest is **118.988871 Mm3**
(delta 11531.493 m3, 0.011531
Mm3). Treated area is **1,063,108.89 ha** across
**427** whole blocks in **126**
tiles.

## 4. Chain v5.1 comparison

| Metric | Unit | v5.1 | Tiled achieved | Delta | Scaled | Delta |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 1.18977e+08 | 1.18989e+08 | 11531.5 | 1.18977e+08 | 1.49012e-08 |
| solid_product_m3 | m3 | 3.76736e+07 | 3.76768e+07 | 3197.27 | 3.76732e+07 | -454.076 |
| sawlog_product_m3 | m3 | 3.3957e+07 | 3.39599e+07 | 2881.85 | 3.39566e+07 | -409.28 |
| panel_product_m3 | m3 | 3.71664e+06 | 3.71695e+06 | 315.422 | 3.71659e+06 | -44.7962 |
| pulp_product_odt | odt | 1.20663e+07 | 1.20676e+07 | 1282.65 | 1.20664e+07 | 113.148 |
| pellet_product_odt | odt | 5.22969e+06 | 5.23038e+06 | 688.953 | 5.22987e+06 | 182.065 |
| bio_product_mwh | MWh | 930946 | 931069 | 122.642 | 930978 | 32.4097 |
| process_residue_m3 | m3 | 5.991e+07 | 5.99158e+07 | 5740.47 | 5.991e+07 | -66.1038 |
| process_residue_odt | odt | 2.69595e+07 | 2.69621e+07 | 2583.21 | 2.69595e+07 | -29.7467 |
| process_residue_pj | PJ | 498.751 | 498.799 | 0.0477894 | 498.75 | -0.000550314 |
| harvest_residue_gross_odt | odt | 2.40222e+07 | 2.40248e+07 | 2644.08 | 2.40225e+07 | 315.778 |
| harvest_residue_gross_pj | PJ | 444.411 | 444.46 | 0.0489155 | 444.417 | 0.00584189 |
| harvest_residue_recoverable_r035_odt | odt | 8.40777e+06 | 8.4087e+06 | 925.429 | 8.40788e+06 | 110.522 |
| harvest_residue_recoverable_r035_pj | PJ | 155.544 | 155.561 | 0.0171204 | 155.546 | 0.00204466 |
| harvest_residue_recoverable_r060_odt | odt | 1.44133e+07 | 1.44149e+07 | 1586.45 | 1.44135e+07 | 189.467 |
| harvest_residue_recoverable_r060_pj | PJ | 266.646 | 266.676 | 0.0293493 | 266.65 | 0.00350514 |
| harvest_residue_recoverable_r075_odt | odt | 1.80167e+07 | 1.80186e+07 | 1983.06 | 1.80169e+07 | 236.834 |
| harvest_residue_recoverable_r075_pj | PJ | 333.308 | 333.345 | 0.0366867 | 333.312 | 0.00438142 |
| total_residue_gross_pj | PJ | 943.162 | 943.258 | 0.096705 | 943.167 | 0.00529158 |
| total_residue_recoverable_r035_pj | PJ | 654.295 | 654.36 | 0.0649099 | 654.296 | 0.00149435 |
| total_residue_recoverable_r060_pj | PJ | 765.397 | 765.475 | 0.0771388 | 765.4 | 0.00295482 |
| total_residue_recoverable_r075_pj | PJ | 832.059 | 832.143 | 0.0844761 | 832.063 | 0.00383111 |

The `ws4_achieved` basis applies the frozen v5.1 per-province coefficients to
the exact tiled harvest. The `scaled_to_119m_control` basis uses one national
factor `0.999903087632` preserving tiled provincial
shares and matching the 118.9773391 Mm3 control total.

## 5. WS4 sample simulation

| Tile | Province | Blocks | Exact m3 | Simulated m3 | Delta m3 |
|---|---|---|---|---|---|
| E30-NB-S13 | NB | 30 | 934650.983455 | 934650.983455 | -1.164e-10 |
| F33-NS-S32 | NS | 1 | 284530.134659 | 284530.134659 | 0.000e+00 |
| T6-NT-S22 | NT | 1 | 901.457172 | 901.457172 | -1.137e-13 |

Each sampled tile was independently validated and simulated for one year with
`CC` at offset 0. Simulated harvested volume equals exact selected block volume
and simulated treated area equals exact selected fragment area within
1e-9 relative tolerance.

## 6. OSeCAN

Rebuilt from the tiled 30-m WS4 chain on the origin-province basis using the frozen handoff-v10 zone weights. Frozen v5.1 21/21 positions match handoff v10; the tiled 119 Mm3 primary basis matches 7/7 and the achieved basis 7/7. Official OSeCAN is unchanged.

## 7. Caveats

- The schedule is a whole-block arithmetic verification, not a sustainable
  harvest, AAC, policy result, or investment case.
- Pass 1 uses the block-offset curve value; pass 2 uses exact fragment ages.
  The exact/approximate ratio is reported per province.
- The candidate pool is a documented top-per-tile volume screen, not a claim
  that smaller blocks are inoperable.
- 30-m forest-area fragments and group RSYC curves are inventory
  realisations, not operable or tenure-feasible areas.
- One `CC` treatment at offset 0 is simulated on the sample tiles. Planting
  response, silviculture, fertilization, and genetic gain are not modelled.
- Product and residue values apply frozen v5.1 coefficients by origin
  province. Facility assignment, mill capacity, transport, and
  interprovincial trade are not re-run.
- The scaled basis is one national factor preserving tiled shares, not
  per-province target scaling.
- 0.60 harvest recovery is a reference case, not a calibrated recovery factor.
- No official OSeCAN file, frozen chain v5.1 artifact, national 990-m dataset,
  or tiled dataset is changed.

## 8. Reproduce

```bash
.venv/bin/python -m workflows.national.facilities.ws4_tiled_chain_119m --workers 32
```
