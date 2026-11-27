# WS4 tiled 30-m dataset — I2|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I2|BC|S23` (parent `I2|BC`)
- Tile / row / col: `I2` / 2 / 3
- Province: `BC`
- Centroid: 52.033881, -127.072958
- Allocated harvest: 118039.713089 m3
- Productive subcell area: 160430.235317 ha
- Committed geometry area: 236469.611265 ha
- Clipped inventory geometry: 236469.611265 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1800763
- Blocks: 1008351
- Forest area: 162068.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 96219
- Scheduled area: 14753.16 ha
- Eligible blocks (age class >= 40): 962187
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.00 MB
- Schedules: 1.14 MB
- Runs: 0.00 MB
- Total: 27.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
