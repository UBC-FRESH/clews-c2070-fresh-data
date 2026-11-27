# WS4 tiled 30-m dataset — L31|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L31|NL|S13` (parent `L31|NL`)
- Tile / row / col: `L31` / 1 / 3
- Province: `NL`
- Centroid: 54.129142, -57.479834
- Allocated harvest: 2728.383617 m3
- Productive subcell area: 46004.676201 ha
- Committed geometry area: 82775.698825 ha
- Clipped inventory geometry: 82775.698825 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 513336
- Blocks: 208100
- Forest area: 46200.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15445
- Scheduled area: 3239.10 ha
- Eligible blocks (age class >= 40): 154445
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.13 MB
- Schedules: 0.18 MB
- Runs: 0.00 MB
- Total: 7.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
