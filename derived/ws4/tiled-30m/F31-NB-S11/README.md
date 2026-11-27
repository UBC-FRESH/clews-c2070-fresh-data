# WS4 tiled 30-m dataset — F31|NB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F31|NB|S11` (parent `F31|NB`)
- Tile / row / col: `F31` / 1 / 1
- Province: `NB`
- Centroid: 47.646068, -65.187284
- Allocated harvest: 110921.227438 m3
- Productive subcell area: 125016.359154 ha
- Committed geometry area: 150745.027921 ha
- Clipped inventory geometry: 150745.027921 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1455260
- Blocks: 504288
- Forest area: 130973.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38413
- Scheduled area: 8818.29 ha
- Eligible blocks (age class >= 40): 384123
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.80 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 18.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
