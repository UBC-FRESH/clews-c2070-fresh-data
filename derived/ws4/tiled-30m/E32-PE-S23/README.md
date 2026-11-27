# WS4 tiled 30-m dataset — E32|PE|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|PE|S23` (parent `E32|PE`)
- Tile / row / col: `E32` / 2 / 3
- Province: `PE`
- Centroid: 46.026042, -62.784089
- Allocated harvest: 15484.873249 m3
- Productive subcell area: 14329.709449 ha
- Committed geometry area: 31757.077608 ha
- Clipped inventory geometry: 31757.077608 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 205267
- Blocks: 83470
- Forest area: 18474.03 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6523
- Scheduled area: 1325.79 ha
- Eligible blocks (age class >= 40): 65229
- Simulated years: 20
- Harvested volume: 167550.327 m3
- Treated/managed area: 1325.790 ha

## Storage

- Dataset: 3.25 MB
- Schedules: 0.07 MB
- Runs: 1.45 MB
- Total: 4.78 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
