# WS4 tiled 30-m dataset — E30|NB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E30|NB|S32` (parent `E30|NB`)
- Tile / row / col: `E30` / 3 / 2
- Province: `NB`
- Centroid: 47.715818, -66.708814
- Allocated harvest: 250236.701286 m3
- Productive subcell area: 236740.658452 ha
- Committed geometry area: 249577.617098 ha
- Clipped inventory geometry: 249577.617098 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2664578
- Blocks: 891285
- Forest area: 239812.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74686
- Scheduled area: 16656.66 ha
- Eligible blocks (age class >= 40): 746857
- Simulated years: 20
- Harvested volume: 3337008.079 m3
- Treated/managed area: 16656.660 ha

## Storage

- Dataset: 31.77 MB
- Schedules: 0.89 MB
- Runs: 18.23 MB
- Total: 50.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
