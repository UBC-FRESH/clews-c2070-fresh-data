# WS4 tiled 30-m dataset — I29|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I29|NL|S11` (parent `I29|NL`)
- Tile / row / col: `I29` / 1 / 1
- Province: `NL`
- Centroid: 52.564613, -66.101982
- Allocated harvest: 5593.415112 m3
- Productive subcell area: 105735.609668 ha
- Committed geometry area: 187894.551264 ha
- Clipped inventory geometry: 187894.551264 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 876668
- Blocks: 311024
- Forest area: 78900.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28389
- Scheduled area: 7147.89 ha
- Eligible blocks (age class >= 40): 283883
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.87 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 11.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
