# E2 v3 density-calibrated tree lists

Status: E2c screening artifact, `model_estimate=true`, `observed=false`,
`policy_grade=false`, `national_claim=false`. No request, DUA, restricted
data, UI change or official OSeCAN change is involved.

## Scope

E2 v3 keeps the E2 v2 geometry, species distribution, donor tapers and
bucking logic, and replaces the uniform 1,000 stems/ha expansion with
province-specific open-inventory density where available. AB, MB and the
four donor-only provinces are explicitly labelled proxy/donor evidence.

## Density sources

| Province | Density stems/ha | Evidence | Basis |
|---|---:|---|---|
| AB | 1000.00 | proxy | AVI DENSITY and STRUC are classes, not numeric stems/ha; the 1,000 stems/ha screening default is retained as a labelled proxy |
| SK | 2033.65 | open_inventory | N = BA / (pi/4 * (QMD/100)^2) per FRI stand, hectare-weighted median; MSTEMS retained as merchantable-stem cross-check |
| MB | 2050.00 | donor | median sum of measured donor expansion factors per donor plot; MB open 1970s FRI has species and age but no density field |
| ON | 1000.00 | proxy | no open stand density field identified; the 1,000 stems/ha screening default is retained as a labelled proxy |
| NS | 1409.82 | open_inventory | N = TOTBA / (pi/4 * (AVDI/100)^2) per polygon, hectare-weighted median; TOTMRVOL retained as the volume check |
| PE | 802.84 | open_inventory | EFI2020 tphmerch, grid-cell-area-weighted median; ba, bamerch and gtv retained as supporting fields and volume check |
| NL | 1000.00 | proxy | no open stand density field identified; the 1,000 stems/ha screening default is retained as a labelled proxy |
| NT | 1000.00 | proxy | no open stand density field identified; the 1,000 stems/ha screening default is retained as a labelled proxy |
| NU | 1000.00 | proxy | no open stand density field identified; the 1,000 stems/ha screening default is retained as a labelled proxy |

## Volume comparison v2 to v3

| Province | Density v2 | Density v3 | Volume v2 | Volume v3 | Ratio | Open volume | Ratio v3/open | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| AB | 1000.00 | 1000.00 | 409.09 | 409.09 | 1.0000 | 0.00 | 0.0000 | not_available |
| SK | 1000.00 | 2033.65 | 43.61 | 88.69 | 2.0336 | 100.13 | 0.8858 | within_50pct |
| MB | 1000.00 | 2050.00 | 122.71 | 251.57 | 2.0500 | 0.00 | 0.0000 | not_available |
| ON | 1000.00 | 1000.00 | 122.91 | 122.91 | 1.0000 | 0.00 | 0.0000 | not_available |
| NS | 1000.00 | 1409.82 | 108.06 | 152.34 | 1.4098 | 105.24 | 1.4476 | within_50pct |
| PE | 1000.00 | 802.84 | 145.48 | 116.79 | 0.8028 | 170.82 | 0.6837 | within_50pct |
| NL | 1000.00 | 1000.00 | 178.40 | 178.40 | 1.0000 | 0.00 | 0.0000 | not_available |
| NT | 1000.00 | 1000.00 | 146.15 | 146.15 | 1.0000 | 0.00 | 0.0000 | not_available |
| NU | 1000.00 | 1000.00 | 102.73 | 102.73 | 1.0000 | 0.00 | 0.0000 | not_available |

## SK / NS / PE

- SK: FRI `BA` and `QMD` imply arithmetic stem density; `MSTEMS` is a
  merchantable-stem cross-check and is not used as total density.
  The v3 volume is compared with FRI `GBVOL`.
- NS: `TOTBA` and `AVDI` imply arithmetic stem density; v3 volume is
  compared with `TOTMRVOL`.
- PE: EFI2020 `tphmerch` is the density target; v3 volume is compared
  with `gtv`.

## Remaining gaps

- AB AVI publishes crown-density and structure classes, not stems/ha.
  The 1,000 stems/ha target is a labelled proxy; class shares are in
  the density evidence artifact.
- MB has no open density field; the median measured donor plot density
  is used and labelled donor evidence.
- ON, NL, NT and NU remain donor-only; the 1,000 stems/ha target is a
  labelled proxy.
- Tapers remain published cross-jurisdiction donors; no local taper is
  claimed. This is not E1 measurement and not a national supply claim.
