# WS4 tiled 30-m dataset — K12|SK|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K12|SK|S31` (parent `K12|SK`)
- Tile / row / col: `K12` / 3 / 1
- Province: `SK`
- Centroid: 59.551864, -107.552095
- Allocated harvest: 15924.546966 m3
- Productive subcell area: 142937.039976 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1970825
- Blocks: 335419
- Forest area: 177374.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24796
- Scheduled area: 9425.88 ha
- Eligible blocks (age class >= 40): 247958
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.64 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 17.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
