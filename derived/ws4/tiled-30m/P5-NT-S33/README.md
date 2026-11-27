# WS4 tiled 30-m dataset — P5|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P5|NT|S33` (parent `P5|NT`)
- Tile / row / col: `P5` / 3 / 3
- Province: `NT`
- Centroid: 62.895278, -129.515918
- Allocated harvest: 16.316901 m3
- Productive subcell area: 27625.431393 ha
- Committed geometry area: 74108.934819 ha
- Clipped inventory geometry: 74108.934819 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 361633
- Blocks: 159754
- Forest area: 32546.97 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11608
- Scheduled area: 2309.85 ha
- Eligible blocks (age class >= 40): 116079
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.55 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 5.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
