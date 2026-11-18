# RSYC Tile-Production v0 National Supply

**Label: RSYC-only v0, no local corrections.** Benchmark correction factors are withheld and were not applied.

Generated 2026-11-18T22:33:22+00:00 from the tile-level production library
(`data/derived/national/assortments/rsyc_tile_production/rsyc_tile_production_library.csv`), 3,948 tile x province x species cells
covering 422.48 Mha.

## Method

- V100 = b1*exp(-b4*100)*(1-exp(-b2*100))^b3 (m3/ha), evaluated per cell; total volume = V100 * area_ha.
- Province residue factors are derived from the diagnostic batch matrix on a **total-volume basis**:
  sum(residue_odt) / sum(volume_m3) after species x ecoprovince area apportionment to provinces.
- Species and group cells use the province factor; no species-specific factor is invented.
- The province factor is applied uniformly to species and group cells and is independent of evidence tier;
  tiers are reported for transparency, not used to weight residue.
- Recovery 0.35 / 0.60 / 0.75; LHV 18.5 GJ/ODT; cost $2.456978/GJ base, 1.30x low, 0.80x high.

## V100 and volume

- National standing volume: **55.244132 B m3** on 422.48 Mha
  (mean 130.8 m3/ha).
- Diagnostic batch total volume: 55.274978 B m3.
  Tile library volume differs by -0.056% (production library, not the diagnostic batch).

### By province

| Province | Area (Mha) | Volume (B m3) | ODT/m3 total | Residue (Mt ODT) | Recoverable PJ base | Diagnostic residue (Mt ODT) | Delta |
|---|---:|---:|---:|---:|---:|---:|---:|
| AB | 38.35 | 6.816 | 0.077980 | 531.5 | 5900.10 | 522.2 | +1.79% |
| BC | 66.61 | 15.895 | 0.078663 | 1250.3 | 13878.81 | 1242.3 | +0.65% |
| MB | 33.75 | 2.959 | 0.127235 | 376.5 | 4179.29 | 397.1 | -5.17% |
| NB | 6.69 | 1.201 | 0.054305 | 65.2 | 724.17 | 56.8 | +14.78% |
| NL | 23.53 | 1.692 | 0.178704 | 302.5 | 3357.23 | 317.1 | -4.62% |
| NS | 4.73 | 0.669 | 0.057259 | 38.3 | 425.02 | 39.9 | -3.94% |
| NT | 43.46 | 3.240 | 0.152144 | 492.9 | 5471.69 | 497.3 | -0.87% |
| NU | 2.83 | 0.119 | 0.163318 | 19.4 | 215.30 | 22.9 | -15.41% |
| ON | 68.52 | 8.887 | 0.074318 | 660.4 | 7330.92 | 611.2 | +8.05% |
| PE | 0.27 | 0.038 | 0.099365 | 3.7 | 41.37 | 3.2 | +15.20% |
| QC | 81.66 | 9.004 | 0.067919 | 611.6 | 6788.45 | 625.6 | -2.25% |
| SK | 26.16 | 2.419 | 0.119641 | 289.4 | 3211.96 | 336.3 | -13.95% |
| YT | 25.91 | 2.305 | 0.102907 | 237.2 | 2633.01 | 253.1 | -6.30% |
| **Total** | 422.48 | 55.244 | 0.088318 | 4879.0 | 54157.32 | 4925.1 | -0.93% |

### By evidence tier

| Tier | Cells | Area share | Volume share | Residue share | PJ share |
|---|---:|---:|---:|---:|---:|
| exact | 1143 | 59.67% | 49.43% | 51.88% | 51.88% |
| group | 2592 | 39.01% | 49.73% | 47.09% | 47.09% |
| generic | 213 | 1.32% | 0.83% | 1.04% | 1.04% |
| control_fallback | 0 | 0.00% | 0.00% | 0.00% | 0.00% |

## Residue factors (m3 total volume basis vs log basis)

- Matrix national total-basis factor: **0.089101080 ODT/m3**;
  diagnostic log-basis factor 0.116820637 ODT/m3
  (total/log ratio 0.7627).
- Tile-weighted factor after applying province factors to tile-library volume:
  **0.088317765 ODT/m3**. It is below the matrix
  national factor through province volume composition: the tile library holds a higher volume
  share in ON and a lower share in SK than the diagnostic matrix, and ON has a low factor
  while SK has a high factor.
- A total-basis factor is the correct multiplier for RSYC gross volume; the diagnostic batch splits
  55.275 B m3 into
  42.159 B m3 log and
  13.116 B m3 residue.
- Province factors range 0.054305 (NB) to
  0.178704 (NL) ODT/m3 total.
- Province factors are area-share apportionments of ecoprovince taper models, not province-specific fits.

## Supply (standing stock at age 100)

- Gross residue: **4.879038 B ODT**
  (12.993255 B m3 at the diagnostic effective density
  0.375505 ODT/m3).
- Recoverable ODT: low 1.707663 B, base
  2.927423 B, high 3.659279 B.
- Recoverable energy (one-time standing stock): low 31591.773 PJ, base
  **54157.325 PJ**, high 67696.656 PJ.
- The **54157.325 PJ** figure is a
  hypothetical all-hectares-at-age-100 standing-stock equivalent, **not an annual cap** and not an
  adopted harvest level.
- Equivalent per 100 million m3 of total volume on the tile mix: low
  57.19 PJ, base
  98.03 PJ, high
  122.54 PJ.
- Base variable cost: 2.456978 $/GJ; standing-stock cost
  equivalent 133063.4 M$ (one-time, not annual).
- Diagnostic batch residue: 4.925060 B ODT; tile library
  differs by -0.934%.

## Harvest sensitivity (matrix-basis vs tile-mix)

Both scenarios use residue ODT per m3 of **total** volume. The matrix-basis rows reproduce the
diagnostic national factor; the tile-mix rows apply the tile library's own volume-weighted factor
and are the tile production estimate. Every row states its volume basis and factor source in the CSV.

| Scenario | Volume basis | Harvest (M m3/yr) | Case | Factor (ODT/m3) | Recoverable PJ/yr | Diagnostic PJ/yr | vs BC 43.52 PJ |
|---|---|---:|---|---:|---:|---:|---:|
| matrix_basis | total_volume_m3_per_year | 100 | low | 0.089101080 | 57.69 | 75.64 | 1.326 |
| matrix_basis | total_volume_m3_per_year | 100 | base | 0.089101080 | 98.90 | 129.67 | 2.272 |
| matrix_basis | total_volume_m3_per_year | 100 | high | 0.089101080 | 123.63 | 162.09 | 2.840 |
| matrix_basis | total_volume_m3_per_year | 150 | low | 0.089101080 | 86.54 | 113.46 | 1.988 |
| matrix_basis | total_volume_m3_per_year | 150 | base | 0.089101080 | 148.35 | 194.51 | 3.409 |
| matrix_basis | total_volume_m3_per_year | 150 | high | 0.089101080 | 185.44 | 243.13 | 4.261 |
| matrix_basis | total_volume_m3_per_year | 200 | low | 0.089101080 | 115.39 | 151.28 | 2.651 |
| matrix_basis | total_volume_m3_per_year | 200 | base | 0.089101080 | 197.80 | 259.34 | 4.545 |
| matrix_basis | total_volume_m3_per_year | 200 | high | 0.089101080 | 247.26 | 324.18 | 5.681 |
| matrix_basis | total_volume_m3_per_year | 250 | low | 0.089101080 | 144.23 | 189.10 | 3.314 |
| matrix_basis | total_volume_m3_per_year | 250 | base | 0.089101080 | 247.26 | 324.18 | 5.681 |
| matrix_basis | total_volume_m3_per_year | 250 | high | 0.089101080 | 309.07 | 405.22 | 7.101 |
| tile_mix | total_volume_m3_per_year | 100 | low | 0.088317765 | 57.19 | 75.64 | 1.314 |
| tile_mix | total_volume_m3_per_year | 100 | base | 0.088317765 | 98.03 | 129.67 | 2.252 |
| tile_mix | total_volume_m3_per_year | 100 | high | 0.088317765 | 122.54 | 162.09 | 2.815 |
| tile_mix | total_volume_m3_per_year | 150 | low | 0.088317765 | 85.78 | 113.46 | 1.971 |
| tile_mix | total_volume_m3_per_year | 150 | base | 0.088317765 | 147.05 | 194.51 | 3.379 |
| tile_mix | total_volume_m3_per_year | 150 | high | 0.088317765 | 183.81 | 243.13 | 4.223 |
| tile_mix | total_volume_m3_per_year | 200 | low | 0.088317765 | 114.37 | 151.28 | 2.628 |
| tile_mix | total_volume_m3_per_year | 200 | base | 0.088317765 | 196.07 | 259.34 | 4.505 |
| tile_mix | total_volume_m3_per_year | 200 | high | 0.088317765 | 245.08 | 324.18 | 5.631 |
| tile_mix | total_volume_m3_per_year | 250 | low | 0.088317765 | 142.96 | 189.10 | 3.285 |
| tile_mix | total_volume_m3_per_year | 250 | base | 0.088317765 | 245.08 | 324.18 | 5.631 |
| tile_mix | total_volume_m3_per_year | 250 | high | 0.088317765 | 306.35 | 405.22 | 7.039 |

The annual rows assume a harvested volume and mix on a total-volume basis; **no adopted national
AAC, THLB, or operability filter is applied**. The BC-only 43.523816 PJ comparison is a scale
comparison, not a like-for-like annual supply comparison.

## B25 and tile capacity

B25 carries 2,736,706.207 ha against a 2,250,000.000 ha polygon (area/polygon_area 1.216314, excess 486,706.207 ha). It is flagged `over_capacity=true` in `rsyc_tile_supply_by_tile.csv` and the summary, not clipped.

## Validation

| Check | Status | Value |
|---|---|---|
| area_sum_matches_expected | PASS | 422475761.522437 ha |
| v100_finite_non_negative | PASS | 3948 cells |
| total_volume_positive | PASS | 55244132111.077461 m3 |
| residue_odt_finite_non_negative | PASS | 4879038251.415109 ODT |
| province_factors_complete | PASS | 13 provinces |
| province_factors_match_backbone_keys | PASS | matrix ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT'] vs backbone ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT'] |
| province_rollup_reconciles_independently | PASS | area 0 ha, volume 0 m3, ODT 0, PJ 0 |
| tile_rollup_reconciles_independently | PASS | area 0 ha, volume 0 m3, ODT 0, PJ 0 |
| evidence_rollup_reconciles_independently | PASS | area 0 ha, volume 0 m3, ODT 0, PJ 7.27596e-12 |
| rollup_values_finite_non_negative | PASS | province, tile, evidence tables |
| evidence_shares_sum_to_one | PASS | volume, area, residue, PJ shares |
| four_evidence_tiers_present | PASS | 4 tiers |
| province_log_factor_reproduces_backbone | PASS | max relative error 6.883e-09 |
| diagnostic_national_factor_reproduces_backbone | PASS | 0.089101080398 ODT/m3 total |
| no_nan_in_outputs | PASS | all emitted aggregates finite |
| tile_weighted_factor_within_province_range | PASS | 0.088317765 ODT/m3 total |
| tile_capacity_flags_are_consistent | PASS | 385 tiles |
| b25_over_capacity_is_flagged_not_clipped | PASS | ratio 1.216314, excess 486706.207 ha |
| harvest_scenarios_are_complete_and_basis_labelled | PASS | 24 rows |
| harvest_rows_recompute_from_factor_and_recovery | PASS | max error 0.000e+00 PJ |
| tile_mix_scenario_uses_tile_weighted_factor | PASS | 0.088317764529 ODT/m3 |
| matrix_scenario_uses_matrix_factor | PASS | 0.089101080398 ODT/m3 |

- Area sum: 422475761.52 ha (expected 422,475,761.52 ha).
- Province, tile, and evidence rollups are each reconciled to independent national area, volume,
  residue ODT, and PJ totals.

## Caveats

- RSYC-only v0: no local corrections, benchmark correction factors withheld.
- Annual harvest rows assume a harvested volume and mix expressed on a total-volume basis; no adopted national AAC, THLB, or operability filter is applied.
- The BC-only 43.523816 PJ value is a scale comparison, not a like-for-like annual supply comparison.
- The national all-hectares-at-age-100 stock equivalent is a hypothetical one-time standing-stock figure, not an annual cap.
- The 0.64% diagnostic gap (419.79 of 422.48 Mha emitted; failed PINU.BAN Great Bear Lowlands cell plus 0.69 Mha other gap) does not apply to the tile library, which covers all area.
- Residue is taper/bucking residue scaled from the diagnostic batch, not full aboveground slash.
- Province residue factors are area-share apportionments, not province-specific taper models.
- Recovery (0.35/0.60/0.75) and cost ($2.456978/GJ, 1.30x/0.80x) are uniform envelopes.
- Group cells (BROADLEAF, CONIFEROUS) use group RSYC curves; they are flagged by evidence_tier=rsyc_tile_group and are not species-exact fits.
- Generic cells use the tile generic RSYC curve; they are flagged by evidence_tier=rsyc_tile_generic.
