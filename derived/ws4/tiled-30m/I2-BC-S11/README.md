# WS4 tiled 30-m dataset — I2|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I2|BC|S11` (parent `I2|BC`)
- Tile / row / col: `I2` / 1 / 1
- Province: `BC`
- Centroid: 51.228074, -127.692073
- Allocated harvest: 15518.924389 m3
- Productive subcell area: 21092.093724 ha
- Committed geometry area: 31089.147215 ha
- Clipped inventory geometry: 31089.147215 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 326735
- Blocks: 176088
- Forest area: 29406.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17485
- Scheduled area: 2886.30 ha
- Eligible blocks (age class >= 40): 174842
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.49 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 5.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
