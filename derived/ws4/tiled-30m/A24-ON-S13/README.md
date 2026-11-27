# WS4 tiled 30-m dataset — A24|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A24|ON|S13` (parent `A24|ON`)
- Tile / row / col: `A24` / 1 / 3
- Province: `ON`
- Centroid: 44.343692, -79.922129
- Allocated harvest: 28617.193659 m3
- Productive subcell area: 109940.439871 ha
- Committed geometry area: 229138.475445 ha
- Clipped inventory geometry: 229138.475445 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 967170
- Blocks: 389779
- Forest area: 87045.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29565
- Scheduled area: 7107.39 ha
- Eligible blocks (age class >= 40): 295650
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.51 MB
- Schedules: 0.35 MB
- Runs: 0.00 MB
- Total: 12.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
