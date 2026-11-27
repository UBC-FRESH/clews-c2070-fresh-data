# WS4 tiled 30-m dataset — F2|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F2|BC|S23` (parent `F2|BC`)
- Tile / row / col: `F2` / 2 / 3
- Province: `BC`
- Centroid: 48.540371, -124.066877
- Allocated harvest: 103560.573528 m3
- Productive subcell area: 107755.143842 ha
- Committed geometry area: 116224.183807 ha
- Clipped inventory geometry: 116224.183807 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1214571
- Blocks: 358470
- Forest area: 109311.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31919
- Scheduled area: 7974.27 ha
- Eligible blocks (age class >= 40): 319184
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.95 MB
- Schedules: 0.37 MB
- Runs: 0.00 MB
- Total: 14.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
