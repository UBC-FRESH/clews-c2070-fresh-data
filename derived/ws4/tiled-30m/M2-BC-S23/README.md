# WS4 tiled 30-m dataset — M2|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M2|BC|S23` (parent `M2|BC`)
- Tile / row / col: `M2` / 2 / 3
- Province: `BC`
- Centroid: 56.809138, -131.740224
- Allocated harvest: 12470.673446 m3
- Productive subcell area: 24675.670649 ha
- Committed geometry area: 116956.337032 ha
- Clipped inventory geometry: 116956.337032 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 554604
- Blocks: 292830
- Forest area: 49914.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26985
- Scheduled area: 4569.84 ha
- Eligible blocks (age class >= 40): 269850
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.56 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 8.87 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
