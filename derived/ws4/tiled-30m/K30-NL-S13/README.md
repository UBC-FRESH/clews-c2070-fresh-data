# WS4 tiled 30-m dataset — K30|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K30|NL|S13` (parent `K30|NL`)
- Tile / row / col: `K30` / 1 / 3
- Province: `NL`
- Centroid: 53.886999, -60.682025
- Allocated harvest: 10055.424619 m3
- Productive subcell area: 164665.481190 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1969295
- Blocks: 486038
- Forest area: 177236.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44414
- Scheduled area: 16477.65 ha
- Eligible blocks (age class >= 40): 444139
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.43 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 20.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
