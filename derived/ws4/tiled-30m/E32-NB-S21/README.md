# WS4 tiled 30-m dataset — E32|NB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|NB|S21` (parent `E32|NB`)
- Tile / row / col: `E32` / 2 / 1
- Province: `NB`
- Centroid: 46.147534, -64.144062
- Allocated harvest: 25643.935912 m3
- Productive subcell area: 37563.854845 ha
- Committed geometry area: 48060.708674 ha
- Clipped inventory geometry: 48060.708674 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 392016
- Blocks: 122121
- Forest area: 35281.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9102
- Scheduled area: 2276.19 ha
- Eligible blocks (age class >= 40): 91018
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.22 MB
- Schedules: 0.10 MB
- Runs: 0.00 MB
- Total: 5.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
