# WS4 tiled 30-m dataset — G17|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G17|ON|S13` (parent `G17|ON`)
- Tile / row / col: `G17` / 1 / 3
- Province: `ON`
- Centroid: 53.716360, -92.474508
- Allocated harvest: 28714.158822 m3
- Productive subcell area: 197349.409563 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2274683
- Blocks: 769878
- Forest area: 204721.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73421
- Scheduled area: 17658.18 ha
- Eligible blocks (age class >= 40): 734205
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.04 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 27.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
