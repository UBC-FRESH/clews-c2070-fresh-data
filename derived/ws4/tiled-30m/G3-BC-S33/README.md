# WS4 tiled 30-m dataset — G3|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G3|BC|S33` (parent `G3|BC`)
- Tile / row / col: `G3` / 3 / 3
- Province: `BC`
- Centroid: 50.648894, -123.481144
- Allocated harvest: 154987.581386 m3
- Productive subcell area: 177642.598529 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 973718
- Blocks: 533265
- Forest area: 87634.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48077
- Scheduled area: 7082.73 ha
- Eligible blocks (age class >= 40): 480768
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.37 MB
- Schedules: 0.57 MB
- Runs: 0.00 MB
- Total: 14.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
