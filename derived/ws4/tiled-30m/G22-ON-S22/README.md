# WS4 tiled 30-m dataset — G22|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G22|ON|S22` (parent `G22|ON`)
- Tile / row / col: `G22` / 2 / 2
- Province: `ON`
- Centroid: 53.287925, -82.132050
- Allocated harvest: 61.372263 m3
- Productive subcell area: 829.272136 ha
- Committed geometry area: 1735.569561 ha
- Clipped inventory geometry: 1735.569561 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 9103
- Blocks: 4659
- Forest area: 819.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3456
- Scheduled area: 576.09 ha
- Eligible blocks (age class >= 40): 3456
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.22 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
