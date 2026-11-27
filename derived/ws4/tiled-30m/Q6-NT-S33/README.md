# WS4 tiled 30-m dataset — Q6|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q6|NT|S33` (parent `Q6|NT`)
- Tile / row / col: `Q6` / 3 / 3
- Province: `NT`
- Centroid: 64.765890, -128.771689
- Allocated harvest: 25.707972 m3
- Productive subcell area: 42534.431928 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 530580
- Blocks: 288629
- Forest area: 47752.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19395
- Scheduled area: 3060.36 ha
- Eligible blocks (age class >= 40): 193943
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.32 MB
- Schedules: 0.23 MB
- Runs: 0.00 MB
- Total: 8.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
