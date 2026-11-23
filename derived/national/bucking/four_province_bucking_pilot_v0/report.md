# Four-province measured bucking pilot (BC, QC, NB, YT)

**Pilot only.**  Measured tree lists; published local/donor tapers; national dimension-only sorts; `grade=not_assigned`; no synthetic trees; no national claim.

## Sample and expansion

| Province | Source rows | Eligible rows | Eligible expansion (stems/ha) | Taper-supported frame | Selected trees | Selected expansion (stems/ha) | Frame expansion (stems/ha) | Conservation error |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BC | 60,960 | 59,397 | 1,188,462.589 | 347 | 347 | 1,188,462.589 | 1,188,462.589 | 2.328e-10 |
| QC | 506,367 | 96,809 | 2,341,448.000 | 71,194 | 85 | 1,741,186.000 | 1,741,186.000 | 0.000e+00 |
| NB | 548,350 | 86,236 | 4,177,850.000 | 56,236 | 106 | 1,545,725.000 | 1,545,725.000 | 0.000e+00 |
| YT | 17,691 | 13,470 | 336,750.000 | 13,317 | 53 | 332,925.000 | 332,925.000 | 0.000e+00 |

QC/NB/YT use one measured PHF-weighted median stem per mapped taper species x 5 cm DBH stratum; the retained stem receives the stratum expansion total.  BC retains the documented v2 measured 2.5 cm BEC x species strata.  Expansion is preserved exactly within each taper-supported, domain-valid frame.

## Taper coverage

| Province | Taper | Source | Status | Trees | Local expansion share | Proxy species |
|---|---|---|---|---:|---:|---|
| BC | BC-KOZAK2004-AC-SBS; BC-KOZAK2004-AT-ICH; BC-KOZAK2004-BL-ESSF; BC-KOZAK2004-CW-ICH; BC-KOZAK2004-EP-ESSF; BC-KOZAK2004-FD-ICH; BC-KOZAK2004-HM-SBS; BC-KOZAK2004-HW-ICH; BC-KOZAK2004-PL-ESSF; BC-KOZAK2004-SB-SBS; BC-KOZAK2004-SE-ESSF; BC-KOZAK2004-SW-ICH | BC | local_published | 347 | 1.000 | BL, EP, HM, SB, SE, SW |
| QC | QC-SCHNEIDER2013-BOP; QC-SCHNEIDER2013-EPB; QC-SCHNEIDER2013-EPN; QC-SCHNEIDER2013-EPR; QC-SCHNEIDER2013-PET; QC-SCHNEIDER2013-SAB; QC-SCHNEIDER2013-THO | QC | local_published | 85 | 1.000 | none |
| NB | NB-DONOR-SCHNEIDER2013-BOP; NB-DONOR-SCHNEIDER2013-EPB; NB-DONOR-SCHNEIDER2013-EPN; NB-DONOR-SCHNEIDER2013-EPR; NB-DONOR-SCHNEIDER2013-PET; NB-DONOR-SCHNEIDER2013-SAB; NB-DONOR-SCHNEIDER2013-THO | QC | donor_published | 106 | 0.000 | none |
| YT | YT-DONOR-KOZAK2004-AT-BWBS; YT-DONOR-KOZAK2004-B-BWBS; YT-DONOR-KOZAK2004-BL-ESSF; YT-DONOR-KOZAK2004-L-BWBS; YT-DONOR-KOZAK2004-PL-SBS; YT-DONOR-KOZAK2004-S-SBS; YT-DONOR-KOZAK2004-SW-SBS | BC | donor_published | 53 | 0.000 | AT, B, BL, L, PL, S, SW |

Local tapers: BC Kozak (2004) Version 6; QC Schneider (2013).  Donor tapers: NB uses QC Schneider; YT uses BC Kozak.  Species proxies encoded by the project mapping are flagged with `taper_proxy=True`.

## Logs, residue and solid share by province

| Province | Trees | Logs | Recovered (m3/ha) | Residue (m3/ha) | Residue (ODT/ha) | Sawlog share | Pulpwood share | Other share | Solid share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BC | 347 | 1,238 | 165,127.42 | 17,506.42 | 6,700.36 | 0.695 | 0.295 | 0.010 | 0.705 |
| QC | 85 | 319 | 266,152.64 | 40,986.60 | 15,812.10 | 0.342 | 0.642 | 0.016 | 0.358 |
| NB | 106 | 380 | 374,151.71 | 30,623.28 | 11,352.24 | 0.524 | 0.467 | 0.009 | 0.533 |
| YT | 53 | 160 | 30,615.18 | 9,659.42 | 3,767.09 | 0.425 | 0.563 | 0.013 | 0.437 |

Shares are expansion-weighted recovered-log volume.  Solid share is sawlog + other roundwood.  Residue is taper total minus recovered gross logs and includes stump-above-base, top and unmerchantable sections.

## Facility coefficient fit

| Province | Model solid | Facility solid | Solid ratio | Model residue ODT/m3 | Facility residue ODT/m3 | Residue ratio | Eligible expansion share | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| BC | 0.705 | 0.689 | 1.023 | 0.0406 | 0.0762 | 0.532 | 1.000 | outside_20pct |
| QC | 0.358 | 0.689 | 0.520 | 0.0594 | 0.0762 | 0.779 | 0.744 | outside_20pct |
| NB | 0.533 | 0.689 | 0.773 | 0.0303 | 0.0762 | 0.398 | 0.370 | outside_20pct |
| YT | 0.437 | 0.689 | 0.635 | 0.1230 | 0.0762 | 1.614 | 0.989 | outside_20pct |

Facility coefficients are feedstock shares from `facility_product_chain_v1`; harvest residue and facility process residue are different streams.  The comparison is a screening check, not calibration.

## Evidence and limits

- `measured_tree_list=true` for all four provinces; `synthetic=false`.
- `model_estimate=true` on log and residue outputs; `national_claim=false`.
- `taper_evidence=published_table`; residue density, moisture and chip/hog yields are labelled assumptions.
- Unsupported measured species and out-of-domain stems are excluded and counted in `sample_audit.csv`; they are not imputed.
- This is not inventory, not an operational supply estimate, and not an official grade.
