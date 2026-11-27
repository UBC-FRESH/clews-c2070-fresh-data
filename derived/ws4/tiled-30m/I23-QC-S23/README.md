# WS4 tiled 30-m dataset — I23|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I23|QC|S23` (parent `I23|QC`)
- Tile / row / col: `I23` / 2 / 3
- Province: `QC`
- Centroid: 55.473668, -77.308517
- Allocated harvest: 3701.833074 m3
- Productive subcell area: 22254.922119 ha
- Committed geometry area: 46411.307177 ha
- Clipped inventory geometry: 46411.307177 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 279461
- Blocks: 133316
- Forest area: 25151.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10521
- Scheduled area: 2055.33 ha
- Eligible blocks (age class >= 40): 105202
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.67 MB
- Schedules: 0.12 MB
- Runs: 0.00 MB
- Total: 4.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
