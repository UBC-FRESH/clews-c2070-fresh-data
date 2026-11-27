# WS4 tiled 30-m dataset — H10|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H10|AB|S12` (parent `H10|AB`)
- Tile / row / col: `H10` / 1 / 2
- Province: `AB`
- Centroid: 54.177882, -110.056170
- Allocated harvest: 7383.235018 m3
- Productive subcell area: 15186.594932 ha
- Committed geometry area: 21006.424399 ha
- Clipped inventory geometry: 21006.424399 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 189315
- Blocks: 59166
- Forest area: 17038.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5068
- Scheduled area: 1326.60 ha
- Eligible blocks (age class >= 40): 50676
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.65 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 2.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
