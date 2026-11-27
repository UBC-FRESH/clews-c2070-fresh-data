# WS4 tiled 30-m dataset — L28|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L28|QC|S11` (parent `L28|QC`)
- Tile / row / col: `L28` / 1 / 1
- Province: `QC`
- Centroid: 56.863488, -65.151542
- Allocated harvest: 4713.725342 m3
- Productive subcell area: 26873.926323 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 531038
- Blocks: 248181
- Forest area: 47793.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18118
- Scheduled area: 3404.88 ha
- Eligible blocks (age class >= 40): 181178
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.69 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 7.90 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
