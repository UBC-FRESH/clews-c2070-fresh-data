# WS4 tiled 30-m dataset — H18|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H18|MB|S32` (parent `H18|MB`)
- Tile / row / col: `H18` / 3 / 2
- Province: `MB`
- Centroid: 55.989257, -90.751327
- Allocated harvest: 2344.048622 m3
- Productive subcell area: 116244.380347 ha
- Committed geometry area: 189509.617835 ha
- Clipped inventory geometry: 189509.617835 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1538264
- Blocks: 489630
- Forest area: 138443.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42144
- Scheduled area: 11325.15 ha
- Eligible blocks (age class >= 40): 421438
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.06 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 18.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
