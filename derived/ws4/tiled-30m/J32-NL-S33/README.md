# WS4 tiled 30-m dataset — J32|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|NL|S33` (parent `J32|NL`)
- Tile / row / col: `J32` / 3 / 3
- Province: `NL`
- Centroid: 52.099908, -57.228129
- Allocated harvest: 7755.236973 m3
- Productive subcell area: 132439.990096 ha
- Committed geometry area: 169725.542725 ha
- Clipped inventory geometry: 169725.542725 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1294636
- Blocks: 575930
- Forest area: 116517.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50396
- Scheduled area: 9943.02 ha
- Eligible blocks (age class >= 40): 503955
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.60 MB
- Schedules: 0.60 MB
- Runs: 0.00 MB
- Total: 18.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
