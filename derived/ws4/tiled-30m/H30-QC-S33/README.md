# WS4 tiled 30-m dataset — H30|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H30|QC|S33` (parent `H30|QC`)
- Tile / row / col: `H30` / 3 / 3
- Province: `QC`
- Centroid: 51.122346, -63.270853
- Allocated harvest: 49314.550739 m3
- Productive subcell area: 199127.127979 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2203785
- Blocks: 626668
- Forest area: 198340.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58379
- Scheduled area: 18986.22 ha
- Eligible blocks (age class >= 40): 583781
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.95 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 25.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
