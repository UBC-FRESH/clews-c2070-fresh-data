# WS4 tiled 30-m dataset — O5|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O5|NT|S33` (parent `O5|NT`)
- Tile / row / col: `O5` / 3 / 3
- Province: `NT`
- Centroid: 61.773756, -127.964571
- Allocated harvest: 9.834608 m3
- Productive subcell area: 12435.843601 ha
- Committed geometry area: 29997.367536 ha
- Clipped inventory geometry: 29997.367536 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 68889
- Blocks: 31872
- Forest area: 6200.01 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2482
- Scheduled area: 475.20 ha
- Eligible blocks (age class >= 40): 24818
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.25 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
