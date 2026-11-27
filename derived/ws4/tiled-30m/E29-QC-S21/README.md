# WS4 tiled 30-m dataset — E29|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E29|QC|S21` (parent `E29|QC`)
- Tile / row / col: `E29` / 2 / 1
- Province: `QC`
- Centroid: 48.000186, -69.319831
- Allocated harvest: 58040.549818 m3
- Productive subcell area: 99798.449356 ha
- Committed geometry area: 121092.149261 ha
- Clipped inventory geometry: 121092.149261 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 871687
- Blocks: 338882
- Forest area: 78451.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28687
- Scheduled area: 6532.65 ha
- Eligible blocks (age class >= 40): 286869
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.32 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 11.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
