# National Product/Residue Chain v2 (Measured Four-Province Coefficients)

Version 2 replaces the product coefficients for BC, QC, NB and YT with measured bucking-pilot shares. The other nine jurisdictions keep the v1 donor coefficients. All values are model estimates: `observed=false`, `policy_grade=false`; no national supply claim.

## Measured coefficient replacement

| Province | Coefficient | Donor | Measured | Applied | Ratio |
|---|---|---:|---:|---:|---:|
| BC | solid_share | 0.689193 | 0.695281 | 0.695281 | 1.009 |
| BC | pulp_share | 0.308234 | 0.294764 | 0.294764 | 0.956 |
| BC | other_share | 0.080095 | 0.009955 | 0.009955 | 0.124 |
| BC | harvest_residue_odt_per_m3 | 0.076226 | 0.040577 | 0.040577 | 0.532 |
| QC | solid_share | 0.689193 | 0.341993 | 0.341993 | 0.496 |
| QC | pulp_share | 0.308234 | 0.641655 | 0.641655 | 2.082 |
| QC | other_share | 0.080095 | 0.016352 | 0.016352 | 0.204 |
| QC | harvest_residue_odt_per_m3 | 0.076226 | 0.059410 | 0.059410 | 0.779 |
| NB | solid_share | 0.689193 | 0.523792 | 0.523792 | 0.760 |
| NB | pulp_share | 0.308234 | 0.467185 | 0.467185 | 1.516 |
| NB | other_share | 0.080095 | 0.009023 | 0.009023 | 0.113 |
| NB | harvest_residue_odt_per_m3 | 0.076226 | 0.030341 | 0.030341 | 0.398 |
| YT | solid_share | 0.689193 | 0.424617 | 0.424617 | 0.616 |
| YT | pulp_share | 0.308234 | 0.562531 | 0.562531 | 1.825 |
| YT | other_share | 0.080095 | 0.012851 | 0.012851 | 0.160 |
| YT | harvest_residue_odt_per_m3 | 0.076226 | 0.123046 | 0.123046 | 1.614 |

Solid is the measured sawlog-grade share and replaces SAW+PANEL feedstock; the within-solid SAW/PANEL split remains the donor split. Pulp is the measured pulpwood share. Other is the measured other-roundwood share and is routed to PELLET/BIO because the facility chain has no OTHER class. Harvest residue is the measured gross ODT/m3; the recoverable share remains the donor assumption.

## Taper coverage and hardwood limits

| Province | Taper status | Taper jurisdictions | Trees | Taper-supported share of eligible frame | Proxy species |
|---|---|---|---:|---:|---|
| BC | local_published | BC | 347 | 1.000 | BL, EP, HM, SB, SE, SW |
| QC | local_published | QC | 85 | 0.744 | none |
| NB | donor_published | QC | 106 | 0.370 | none |
| YT | donor_published | BC | 53 | 0.989 | AT, B, BL, L, PL, S, SW |

BC and QC use local published tapers (Kozak 2004; Schneider 2013); NB uses the QC donor and YT the BC donor. Species without a mapped taper, stems outside the taper domain, and unsupported hardwoods are excluded and not imputed. The measured coefficients therefore cover only the taper-supported measured frame, not all provincial species or all hardwood volume; BC, NB and YT proxy species remain labelled proxies.

## 119 Mm3 national totals

| Metric | v2 measured |
|---|---:|
| harvest_m3 (m3) | 118,977,339.100 |
| total_feedstock_m3 (m3) | 130,840,334.913 |
| sawlog_product_m3 (m3) | 42,520,151.761 |
| pulp_product_odt (odt) | 9,526,992.918 |
| panel_product_m3 (m3) | 4,653,886.714 |
| pellet_product_odt (odt) | 4,172,333.553 |
| bio_product_mwh (MWh) | 742,724.744 |
| process_residue_odt (odt) | 27,816,973.784 |
| harvest_residue_gross_odt (odt) | 6,911,363.873 |
| harvest_residue_recoverable_odt (odt) | 4,918,372.779 |
| total_residue_gross_odt (odt) | 34,728,337.657 |

## Validation

| Check | Status | Detail |
|---|---|---|
| measured_province_set | PASS | measured=['BC', 'NB', 'QC', 'YT'] |
| donor_province_count | PASS | donor rows=9 |
| grade_conservation | PASS | failed: [] |
| feedstock_conservation | PASS | failed: [] |
| residue_consistency | PASS | failed: [] |
| labels | PASS | failed: [] |
| measured_share_sum | PASS | failed: [] |
| replacement_measured_values | PASS | failed: [] |

## Caveats

- All values are model estimates; observed=false and policy_grade=false.
- Measured product shares are expansion-weighted recovered-log shares from the four-province pilot, not mill receipts or a provincial supply estimate.
- Solid is the measured sawlog share and replaces SAW+PANEL feedstock. The SAW/PANEL split remains a donor split because the pilot does not measure panel logs separately.
- Other roundwood is routed to PELLET/BIO because the facility chain has no OTHER class. That routing and the pellet/bio split are donor assumptions, not measured coefficients.
- Taper coverage is local for BC and QC, donor for NB (QC Schneider) and YT (BC Kozak). Unsupported species and out-of-domain stems are excluded and not imputed; hardwood coverage is limited by the mapped taper species.
- The recoverable share of gross harvest residue and all mill conversion ratios remain donor assumptions from national_product_chain_v1.
- No UI or public OSeCAN surface is changed by this artifact.

Labels: `model_estimate`, `observed=false`, `policy_grade=false`.
