# WS4 tiled 30-m dataset — C32|NS|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C32|NS|S33` (parent `C32|NS`)
- Tile / row / col: `C32` / 3 / 3
- Province: `NS`
- Centroid: 44.099885, -64.613667
- Allocated harvest: 11734.825271 m3
- Productive subcell area: 19540.263860 ha
- Committed geometry area: 23449.352017 ha
- Clipped inventory geometry: 23449.352017 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 220424
- Blocks: 85489
- Forest area: 19838.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7644
- Scheduled area: 1775.61 ha
- Eligible blocks (age class >= 40): 76432
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.43 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 3.51 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
