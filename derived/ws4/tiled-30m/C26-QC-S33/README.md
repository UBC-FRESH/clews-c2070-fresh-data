# WS4 tiled 30-m dataset — C26|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C26|QC|S33` (parent `C26|QC`)
- Tile / row / col: `C26` / 3 / 3
- Province: `QC`
- Centroid: 47.050613, -74.899084
- Allocated harvest: 127938.356993 m3
- Productive subcell area: 207690.437894 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2522271
- Blocks: 810562
- Forest area: 227004.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 70319
- Scheduled area: 18289.71 ha
- Eligible blocks (age class >= 40): 703190
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.96 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 30.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
