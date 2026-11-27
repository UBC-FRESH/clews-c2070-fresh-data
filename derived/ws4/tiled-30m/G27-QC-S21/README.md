# WS4 tiled 30-m dataset — G27|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G27|QC|S21` (parent `G27|QC`)
- Tile / row / col: `G27` / 2 / 1
- Province: `QC`
- Centroid: 51.566646, -71.718089
- Allocated harvest: 51730.942415 m3
- Productive subcell area: 184053.046709 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1915559
- Blocks: 550732
- Forest area: 172400.31 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44966
- Scheduled area: 12133.71 ha
- Eligible blocks (age class >= 40): 449656
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.23 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 21.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
