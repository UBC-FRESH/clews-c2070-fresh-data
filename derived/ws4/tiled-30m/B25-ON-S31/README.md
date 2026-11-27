# WS4 tiled 30-m dataset — B25|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B25|ON|S31` (parent `B25|ON`)
- Tile / row / col: `B25` / 3 / 1
- Province: `ON`
- Centroid: 46.264606, -78.634473
- Allocated harvest: 32478.349384 m3
- Productive subcell area: 112604.097538 ha
- Committed geometry area: 84863.586434 ha
- Clipped inventory geometry: 84863.586434 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 816485
- Blocks: 309142
- Forest area: 73483.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28204
- Scheduled area: 6162.12 ha
- Eligible blocks (age class >= 40): 282035
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.70 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 11.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
