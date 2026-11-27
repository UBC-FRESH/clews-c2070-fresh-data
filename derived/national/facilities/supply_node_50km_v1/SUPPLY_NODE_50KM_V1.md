# 50-km Supply-Node Sensitivity V1

Status: **model-estimate geometric granularity sidecar** — `evidence_label=model_estimate`, `observed=false`, `policy_grade=false`, `sensitivity_only=true`, `chain_v51_unchanged=true`. No national claim, no policy claim, and no official OSeCAN change.

## 1. Method

Each committed 150-km RSYC tile-province supply node from `supply_node_distance_v1` is split into a 3x3 grid of 50-km subcells. The tile bounding box is divided into three equal parts in x and y in EPSG:3978 metres. Each subcell is intersected with the parent tile-province geometry; positive intersections become subnodes.

Parent `production_m3` and `harvest_m3` are allocated to subcells in proportion to the geometric subcell area inside the parent tile-province intersection. Parent production, parent harvest and provincial totals are preserved exactly. The subcell node location is the intersection centroid, replaced by `representative_point()` when the centroid falls outside.

Node IDs use `<tile_id>|<province>|S<row><col>` (for example `E5|BC|S11`).

## 2. Area-proportional assumption

The allocation assumes uniform production density within each parent tile-province cell. This is a geometric granularity test, not new RSYC resolution: no within-tile forest mask, species map, harvest block, cutblock or truck origin is introduced. The 50-km subnode is a location for the parent volume, not an observed harvest point.

The committed `located_area_ha` is the RSYC allocated productive area (the sum of species/group allocation rows), not the full geometric tile-province area. The build therefore validates the geometric 3x3 partition against the reconstructed tile-province geometry and carries the production area as a separate accounting quantity. It does not claim that the two areas are equal.

## 3. Counts and conservation

- Parent nodes: **525**.
- 50-km subnodes: **3,562**.
- Positive-harvest subnodes: **3,359**; zero-harvest subnodes: **203** (NU only).
- Subnodes per parent: min 1, max 9, mean 6.785.
- Parent production: **55,227,876,513.326 m3**; subnode production: **55,227,876,513.326 m3**; residual 0.000000000 m3.
- Parent harvest: **118,977,339.100 m3**; subnode harvest: **118,977,339.100 m3**; residual 0.000000030 m3.
- National harvest: **118,977,339.100 m3** (the committed 118,977,339.1 m3 control total).
- Maximum province weight-sum deviation: 2.265e-14.

## 4. Geometry diagnostics

- Geometric parent area total: **708,967,117.680 ha**.
- Sum of subcell geometric areas: **708,967,117.680 ha**; residual 0.000000000 ha.
- Parents where `located_area_ha` equals the geometric area within tolerance: **0** of **525**.
- `located_area_ha` / geometric area ratio: min 0.000039, median 0.623547, max 1.326884.

The ratio is not one because the committed production area is the RSYC species/group allocation area, not the tile polygon area. The production area is validated against the RSYC library and conserved through the subcell allocation.

## 5. Labels and scope

- `model_estimate`, `observed=false`, `policy_grade=false`.
- `national_claim=false`, `official_osecan_changed=false`, `ui_changed=false`.
- `sensitivity_only=true`, `chain_v51_unchanged=true`.
- No chain v5.1, frozen artifact, UI, portal, or official OSeCAN change is made.

## 6. Reproduce

`.venv/bin/python -m workflows.national.facilities.supply_node_50km_v1`

