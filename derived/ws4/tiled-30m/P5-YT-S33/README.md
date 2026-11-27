# WS4 tiled 30-m dataset — P5|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P5|YT|S33` (parent `P5|YT`)
- Tile / row / col: `P5` / 3 / 3
- Province: `YT`
- Centroid: 62.847881, -129.995176
- Allocated harvest: 125.617417 m3
- Productive subcell area: 124423.433939 ha
- Committed geometry area: 175891.065181 ha
- Clipped inventory geometry: 175891.065181 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 895601
- Blocks: 358812
- Forest area: 80604.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27419
- Scheduled area: 6881.49 ha
- Eligible blocks (age class >= 40): 274181
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.63 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 11.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
