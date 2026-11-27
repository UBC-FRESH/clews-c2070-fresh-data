# WS4 tiled 30-m dataset — D24|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D24|QC|S23` (parent `D24|QC`)
- Tile / row / col: `D24` / 2 / 3
- Province: `QC`
- Centroid: 48.674620, -78.346139
- Allocated harvest: 81426.841295 m3
- Productive subcell area: 205262.645297 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2295965
- Blocks: 924215
- Forest area: 206636.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79046
- Scheduled area: 15748.20 ha
- Eligible blocks (age class >= 40): 790457
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.51 MB
- Schedules: 0.94 MB
- Runs: 0.00 MB
- Total: 30.45 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
