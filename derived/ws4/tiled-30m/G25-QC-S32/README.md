# WS4 tiled 30-m dataset — G25|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G25|QC|S32` (parent `G25|QC`)
- Tile / row / col: `G25` / 3 / 2
- Province: `QC`
- Centroid: 52.754214, -74.953446
- Allocated harvest: 36100.529959 m3
- Productive subcell area: 145164.027264 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1500875
- Blocks: 404412
- Forest area: 135078.75 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26552
- Scheduled area: 5023.71 ha
- Eligible blocks (age class >= 40): 265516
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.72 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 16.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
