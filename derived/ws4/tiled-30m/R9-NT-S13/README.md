# WS4 tiled 30-m dataset — R9|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R9|NT|S13` (parent `R9|NT`)
- Tile / row / col: `R9` / 1 / 3
- Province: `NT`
- Centroid: 67.044062, -120.162631
- Allocated harvest: 2.492509 m3
- Productive subcell area: 6703.253447 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 197127
- Blocks: 110600
- Forest area: 17741.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4647
- Scheduled area: 703.08 ha
- Eligible blocks (age class >= 40): 46465
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.64 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 3.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
