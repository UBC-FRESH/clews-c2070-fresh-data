# Donor Candidate Inventory

Generated: 2026-11-18T16:25:50Z

## Counts

- Batch cells: 1,191
- Mapped positive: 265
- Mapped zero: 159
- Unmapped RSYC species: 767
- Zero SCANFI forest area: 0
- Supply eligible: 1,032
- Target-province weak cells (AB/ON/NS/NU/MB): 398
- Donor rows: 1,911
- No-plot ecodistricts: 371

## Method

0.30 same ecozone + 0.20 distance decay (800 km) + 0.25 exact direct fit / 0.15 exact pooled / 0.05 species-group proxy + 0.15 log10 site support + 0.05 group match + 0.05 donor SCANFI area.

## Caveats

- MGM curves are not joined; all rows carry mgm_join_pending=true.
- Batch cells are ecoprovince-level and can span multiple provinces; target_provinces lists the overlap.
- Donor support is measured by plot counts, not by ecological representativeness or variance compatibility.
- SCANFI resolves ten species/classes; unmapped RSYC species cannot receive SCANFI area.
