# WS4 tiled 30-m dataset — F25|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F25|QC|S21` (parent `F25|QC`)
- Tile / row / col: `F25` / 2 / 1
- Province: `QC`
- Centroid: 51.155757, -76.531497
- Allocated harvest: 29746.222024 m3
- Productive subcell area: 159257.145725 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2012714
- Blocks: 674595
- Forest area: 181144.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51929
- Scheduled area: 11249.55 ha
- Eligible blocks (age class >= 40): 519290
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.49 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 24.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
