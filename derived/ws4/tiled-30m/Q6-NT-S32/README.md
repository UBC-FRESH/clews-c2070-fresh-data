# WS4 tiled 30-m dataset — Q6|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q6|NT|S32` (parent `Q6|NT`)
- Tile / row / col: `Q6` / 3 / 2
- Province: `NT`
- Centroid: 64.528745, -129.698177
- Allocated harvest: 25.707972 m3
- Productive subcell area: 42534.431928 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 568163
- Blocks: 310658
- Forest area: 51134.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22387
- Scheduled area: 3320.55 ha
- Eligible blocks (age class >= 40): 223865
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.82 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 9.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
