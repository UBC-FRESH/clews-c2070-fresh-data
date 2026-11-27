# WS4 tiled 30-m dataset — C26|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C26|QC|S32` (parent `C26|QC`)
- Tile / row / col: `C26` / 3 / 2
- Province: `QC`
- Centroid: 47.187244, -75.521524
- Allocated harvest: 127938.356993 m3
- Productive subcell area: 207690.437894 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2391866
- Blocks: 699364
- Forest area: 215267.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 64314
- Scheduled area: 21209.31 ha
- Eligible blocks (age class >= 40): 643133
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.42 MB
- Schedules: 0.76 MB
- Runs: 0.00 MB
- Total: 28.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
