# WS4 tiled 30-m dataset — D14|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D14|MB|S32` (parent `D14|MB`)
- Tile / row / col: `D14` / 3 / 2
- Province: `MB`
- Centroid: 50.452160, -99.759725
- Allocated harvest: 1077.408846 m3
- Productive subcell area: 23255.748089 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 826763
- Blocks: 281766
- Forest area: 74408.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24544
- Scheduled area: 6495.75 ha
- Eligible blocks (age class >= 40): 245435
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.21 MB
- Schedules: 0.28 MB
- Runs: 0.00 MB
- Total: 10.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
