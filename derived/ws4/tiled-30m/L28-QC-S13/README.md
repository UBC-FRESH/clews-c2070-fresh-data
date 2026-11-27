# WS4 tiled 30-m dataset — L28|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L28|QC|S13` (parent `L28|QC`)
- Tile / row / col: `L28` / 1 / 3
- Province: `QC`
- Centroid: 56.446172, -64.044122
- Allocated harvest: 395.842511 m3
- Productive subcell area: 2256.780297 ha
- Committed geometry area: 20994.143817 ha
- Clipped inventory geometry: 20994.143817 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 5896
- Blocks: 3899
- Forest area: 530.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 525
- Scheduled area: 64.89 ha
- Eligible blocks (age class >= 40): 525
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.18 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
