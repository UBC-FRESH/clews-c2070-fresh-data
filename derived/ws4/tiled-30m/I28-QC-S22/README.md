# WS4 tiled 30-m dataset — I28|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I28|QC|S22` (parent `I28|QC`)
- Tile / row / col: `I28` / 2 / 2
- Province: `QC`
- Centroid: 53.354153, -67.296210
- Allocated harvest: 17174.816507 m3
- Productive subcell area: 111902.070319 ha
- Committed geometry area: 188988.991575 ha
- Clipped inventory geometry: 188988.991575 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1479554
- Blocks: 408031
- Forest area: 133159.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37490
- Scheduled area: 13262.13 ha
- Eligible blocks (age class >= 40): 374892
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.71 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 17.15 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
