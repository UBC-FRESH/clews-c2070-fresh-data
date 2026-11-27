# WS4 tiled 30-m dataset — F25|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F25|QC|S12` (parent `F25|QC`)
- Tile / row / col: `F25` / 1 / 2
- Province: `QC`
- Centroid: 50.591449, -76.054309
- Allocated harvest: 29746.222024 m3
- Productive subcell area: 159257.145725 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1736164
- Blocks: 586429
- Forest area: 156254.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41811
- Scheduled area: 9461.97 ha
- Eligible blocks (age class >= 40): 418104
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.70 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 21.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
