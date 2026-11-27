# WS4 tiled 30-m dataset — D19|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D19|ON|S23` (parent `D19|ON`)
- Tile / row / col: `D19` / 2 / 3
- Province: `ON`
- Centroid: 49.900136, -88.507083
- Allocated harvest: 48562.975834 m3
- Productive subcell area: 185647.724250 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 335631
- Blocks: 164679
- Forest area: 30206.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16139
- Scheduled area: 2936.61 ha
- Eligible blocks (age class >= 40): 161385
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.55 MB
- Schedules: 0.18 MB
- Runs: 0.00 MB
- Total: 5.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
