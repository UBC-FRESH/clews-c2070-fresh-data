# WS4 tiled 30-m dataset — C24|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C24|ON|S13` (parent `C24|ON`)
- Tile / row / col: `C24` / 1 / 3
- Province: `ON`
- Centroid: 46.826419, -79.284502
- Allocated harvest: 6484.366071 m3
- Productive subcell area: 22958.629886 ha
- Committed geometry area: 28007.395394 ha
- Clipped inventory geometry: 28007.395394 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 278579
- Blocks: 114503
- Forest area: 25072.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10584
- Scheduled area: 2062.26 ha
- Eligible blocks (age class >= 40): 105835
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.42 MB
- Schedules: 0.12 MB
- Runs: 0.00 MB
- Total: 4.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
