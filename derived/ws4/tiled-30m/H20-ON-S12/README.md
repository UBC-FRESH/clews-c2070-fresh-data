# WS4 tiled 30-m dataset — H20|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H20|ON|S12` (parent `H20|ON`)
- Tile / row / col: `H20` / 1 / 2
- Province: `ON`
- Centroid: 54.753546, -86.045853
- Allocated harvest: 6398.118908 m3
- Productive subcell area: 112765.261230 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 912980
- Blocks: 485198
- Forest area: 82168.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37867
- Scheduled area: 6745.23 ha
- Eligible blocks (age class >= 40): 378661
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.24 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 13.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
