# WS4 tiled 30-m dataset — D31|NB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D31|NB|S21` (parent `D31|NB`)
- Tile / row / col: `D31` / 2 / 1
- Province: `NB`
- Centroid: 45.724091, -66.655627
- Allocated harvest: 196075.443660 m3
- Productive subcell area: 218596.365827 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2445013
- Blocks: 920668
- Forest area: 220051.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74737
- Scheduled area: 14466.96 ha
- Eligible blocks (age class >= 40): 747370
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.16 MB
- Schedules: 0.89 MB
- Runs: 0.00 MB
- Total: 31.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
