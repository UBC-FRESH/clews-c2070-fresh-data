# WS4 tiled 30-m dataset — J33|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J33|NL|S11` (parent `J33|NL`)
- Tile / row / col: `J33` / 1 / 1
- Province: `NL`
- Centroid: 51.021912, -57.071112
- Allocated harvest: 26.953271 m3
- Productive subcell area: 569.404942 ha
- Committed geometry area: 858.083543 ha
- Clipped inventory geometry: 858.083543 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 3570
- Blocks: 2378
- Forest area: 321.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1910
- Scheduled area: 261.63 ha
- Eligible blocks (age class >= 40): 1910
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.14 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
