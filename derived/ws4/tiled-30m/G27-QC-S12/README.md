# WS4 tiled 30-m dataset — G27|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G27|QC|S12` (parent `G27|QC`)
- Tile / row / col: `G27` / 1 / 2
- Province: `QC`
- Centroid: 50.980500, -71.305126
- Allocated harvest: 51730.942415 m3
- Productive subcell area: 184053.046709 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1943252
- Blocks: 601479
- Forest area: 174892.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44849
- Scheduled area: 11479.14 ha
- Eligible blocks (age class >= 40): 448484
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.47 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 23.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
