# WS4 tiled 30-m dataset — K32|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K32|NL|S23` (parent `K32|NL`)
- Tile / row / col: `K32` / 2 / 3
- Province: `NL`
- Centroid: 52.787927, -56.435990
- Allocated harvest: 10670.971545 m3
- Productive subcell area: 194540.139299 ha
- Committed geometry area: 243512.462910 ha
- Clipped inventory geometry: 243512.462910 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2254305
- Blocks: 696508
- Forest area: 202887.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65442
- Scheduled area: 20181.33 ha
- Eligible blocks (age class >= 40): 654414
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.79 MB
- Schedules: 0.77 MB
- Runs: 0.00 MB
- Total: 26.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
