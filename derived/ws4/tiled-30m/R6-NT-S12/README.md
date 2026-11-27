# WS4 tiled 30-m dataset — R6|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R6|NT|S12` (parent `R6|NT`)
- Tile / row / col: `R6` / 1 / 2
- Province: `NT`
- Centroid: 64.923129, -130.263775
- Allocated harvest: 64.971190 m3
- Productive subcell area: 94649.713824 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 289603
- Blocks: 159661
- Forest area: 26064.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9756
- Scheduled area: 1433.61 ha
- Eligible blocks (age class >= 40): 97553
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.06 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 5.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
