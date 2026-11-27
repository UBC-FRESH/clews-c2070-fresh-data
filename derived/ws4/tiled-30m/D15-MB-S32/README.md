# WS4 tiled 30-m dataset — D15|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D15|MB|S32` (parent `D15|MB`)
- Tile / row / col: `D15` / 3 / 2
- Province: `MB`
- Centroid: 50.530974, -97.637697
- Allocated harvest: 1147.881972 m3
- Productive subcell area: 26936.761457 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1087323
- Blocks: 213825
- Forest area: 97859.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13064
- Scheduled area: 8748.90 ha
- Eligible blocks (age class >= 40): 130633
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.80 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 10.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
