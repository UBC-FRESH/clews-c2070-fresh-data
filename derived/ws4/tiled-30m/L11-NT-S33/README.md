# WS4 tiled 30-m dataset — L11|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L11|NT|S33` (parent `L11|NT`)
- Tile / row / col: `L11` / 3 / 3
- Province: `NT`
- Centroid: 60.811340, -109.036202
- Allocated harvest: 106.464871 m3
- Productive subcell area: 150185.735956 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2023207
- Blocks: 339983
- Forest area: 182088.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14824
- Scheduled area: 4251.60 ha
- Eligible blocks (age class >= 40): 148239
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.85 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 18.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
