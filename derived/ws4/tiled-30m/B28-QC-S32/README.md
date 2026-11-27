# WS4 tiled 30-m dataset — B28|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B28|QC|S32` (parent `B28|QC`)
- Tile / row / col: `B28` / 3 / 2
- Province: `QC`
- Centroid: 45.145486, -72.511306
- Allocated harvest: 48300.003288 m3
- Productive subcell area: 77502.725171 ha
- Committed geometry area: 149590.301641 ha
- Clipped inventory geometry: 149590.301641 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1364821
- Blocks: 362543
- Forest area: 122833.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32233
- Scheduled area: 11476.80 ha
- Eligible blocks (age class >= 40): 322330
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.31 MB
- Schedules: 0.38 MB
- Runs: 0.00 MB
- Total: 15.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
