# WS4 tiled 30-m dataset — B22|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B22|ON|S21` (parent `B22|ON`)
- Tile / row / col: `B22` / 2 / 1
- Province: `ON`
- Centroid: 46.822791, -84.311429
- Allocated harvest: 49062.877443 m3
- Productive subcell area: 167488.302956 ha
- Committed geometry area: 186070.864911 ha
- Clipped inventory geometry: 186070.864911 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1936886
- Blocks: 322043
- Forest area: 174319.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30789
- Scheduled area: 14670.45 ha
- Eligible blocks (age class >= 40): 307889
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.18 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 18.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
