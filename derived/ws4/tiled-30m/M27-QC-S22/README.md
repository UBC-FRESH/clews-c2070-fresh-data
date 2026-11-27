# WS4 tiled 30-m dataset — M27|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M27|QC|S22` (parent `M27|QC`)
- Tile / row / col: `M27` / 2 / 2
- Province: `QC`
- Centroid: 58.915807, -65.163927
- Allocated harvest: 3283.325492 m3
- Productive subcell area: 17923.656804 ha
- Committed geometry area: 229675.918900 ha
- Clipped inventory geometry: 229675.918900 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 135221
- Blocks: 84252
- Forest area: 12169.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5913
- Scheduled area: 873.81 ha
- Eligible blocks (age class >= 40): 59125
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.76 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 2.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
