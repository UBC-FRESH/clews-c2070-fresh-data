# WS4 tiled 30-m dataset — T5|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T5|NT|S23` (parent `T5|NT`)
- Tile / row / col: `T5` / 2 / 3
- Province: `NT`
- Centroid: 67.076169, -136.071146
- Allocated harvest: 1.391410 m3
- Productive subcell area: 1446.373399 ha
- Committed geometry area: 20280.243867 ha
- Clipped inventory geometry: 20280.243867 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 13449
- Blocks: 7074
- Forest area: 1210.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3358
- Scheduled area: 466.11 ha
- Eligible blocks (age class >= 40): 3358
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.30 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
