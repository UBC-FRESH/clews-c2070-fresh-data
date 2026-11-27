# WS4 tiled 30-m dataset — J16|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J16|MB|S33` (parent `J16|MB`)
- Tile / row / col: `J16` / 3 / 3
- Province: `MB`
- Centroid: 58.765191, -94.829170
- Allocated harvest: 882.347397 m3
- Productive subcell area: 64294.265301 ha
- Committed geometry area: 195240.363147 ha
- Clipped inventory geometry: 195240.363147 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 746735
- Blocks: 294845
- Forest area: 67206.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24188
- Scheduled area: 8545.68 ha
- Eligible blocks (age class >= 40): 241876
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.78 MB
- Schedules: 0.28 MB
- Runs: 0.00 MB
- Total: 10.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
