# WS4 tiled 30-m dataset — B28|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B28|QC|S21` (parent `B28|QC`)
- Tile / row / col: `B28` / 2 / 1
- Province: `QC`
- Centroid: 45.032895, -73.430064
- Allocated harvest: 2960.862759 m3
- Productive subcell area: 4751.033480 ha
- Committed geometry area: 9170.110209 ha
- Clipped inventory geometry: 9170.110209 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 67103
- Blocks: 18449
- Forest area: 6039.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1274
- Scheduled area: 335.34 ha
- Eligible blocks (age class >= 40): 12734
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.98 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
