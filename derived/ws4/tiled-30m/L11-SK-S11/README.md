# WS4 tiled 30-m dataset — L11|SK|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L11|SK|S11` (parent `L11|SK`)
- Tile / row / col: `L11` / 1 / 1
- Province: `SK`
- Centroid: 59.617890, -109.956243
- Allocated harvest: 834.093794 m3
- Productive subcell area: 7225.105561 ha
- Committed geometry area: 11513.634257 ha
- Clipped inventory geometry: 11513.634257 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 114486
- Blocks: 18907
- Forest area: 10303.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 673
- Scheduled area: 142.56 ha
- Eligible blocks (age class >= 40): 6722
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.29 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
