# Share-based operable block mask

**Artifact:** `ws4_operable_mask` **Version:** 1.0.0

**Status:** screening proxy. This is not a legal THLB, a slope screen, or a
spatial road overlay.

**Screen case:** `screen_core30` - SCANFI median age >= 30 years, NBAC 2020
burned pixels excluded, block centre within 10 km of a public NRN road.

**Labels:** `share_based_operable_proxy=true`, `legal_thlb=false`,
`slope_screen=false`, `model_estimate=true`, `observed=false`,
`policy_grade=false`, `national_claim=false`.

## 1. Method

Within each province, blocks are ranked by a stable `blake2b(province:block_id)`
hash and taken whole until the selected forest area reaches
`operable_share_of_treed * WS4 province forest area`. The published absolute
`operable_proxy_ha` is reported as a cross-check but is not forced onto the
WS4 block denominator. No block is selected twice. The mask is deterministic.

## 2. Province result

| Province | Coverage | Published share | WS4 forest Mha | Share target Mha | Selected Mha | Selected share | Selected blocks |
|---|---|---:|---:|---:|---:|---:|---:|
| BC | yes | 33.6629% | 65.698 | 22.116 | 22.116 | 33.6630% | 164,442 |
| AB | yes | 28.5791% | 37.550 | 10.732 | 10.731 | 28.5782% | 47,774 |
| SK | yes | 11.2245% | 23.593 | 2.648 | 2.648 | 11.2245% | 12,040 |
| MB | yes | 6.8898% | 31.879 | 2.196 | 2.146 | 6.7301% | 9,272 |
| ON | yes | 33.4358% | 66.682 | 22.296 | 22.317 | 33.4684% | 71,707 |
| QC | yes | 12.8963% | 81.424 | 10.501 | 10.501 | 12.8963% | 45,146 |
| NB | yes | 26.4599% | 6.605 | 1.748 | 1.748 | 26.4598% | 7,685 |
| NS | yes | 18.1834% | 4.674 | 0.850 | 0.850 | 18.1824% | 3,311 |
| PE | no | n/a | 0.269 | 0.000 | 0.000 | 0.0000% | 0 |
| NL | yes | 2.8825% | 23.342 | 0.673 | 0.673 | 2.8828% | 2,660 |
| YT | yes | 5.6880% | 25.809 | 1.468 | 1.468 | 5.6879% | 6,025 |
| NT | yes | 0.4234% | 42.370 | 0.179 | 0.177 | 0.4177% | 690 |
| NU | no | n/a | 1.355 | 0.000 | 0.000 | 0.0000% | 0 |

National selected area: 75.374 Mha
across 370,752 blocks
(18.3280% of WS4 forest
area). Published screen area: 77.050
Mha (18.2377% of SCANFI
treed area). The selected area is
-1.676 Mha
(-2.175%) versus the
published absolute area, because the WS4 block forest denominator is smaller
than the SCANFI treed denominator.

## 3. Gaps and limitations

- No legal THLB boundary.
- No national slope/elevation DEM; no slope screen.
- Road distance is public-NRN Euclidean distance at 990 m, not a spatial road
  overlay; resource/industrial roads are absent.
- NBAC 2020 only; 2010/2015 disturbance cases are gaps.
- SCANFI age is a prediction surface.
- Managed share is uniform inside each province-ecoprovince.
- NU and PE have no 2016 tenure coverage and intentionally have no operable
  blocks.
