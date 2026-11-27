# WS4 tiled 30-m dataset — E32|NS|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|NS|S13` (parent `E32|NS`)
- Tile / row / col: `E32` / 1 / 3
- Province: `NS`
- Centroid: 45.504778, -63.262673
- Allocated harvest: 92326.817652 m3
- Productive subcell area: 196905.102904 ha
- Committed geometry area: 243358.554312 ha
- Clipped inventory geometry: 243358.554312 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2190554
- Blocks: 692058
- Forest area: 197149.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50072
- Scheduled area: 10175.13 ha
- Eligible blocks (age class >= 40): 500718
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.16 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 25.75 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
