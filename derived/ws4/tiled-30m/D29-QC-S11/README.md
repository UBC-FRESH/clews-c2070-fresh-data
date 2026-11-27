# WS4 tiled 30-m dataset — D29|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D29|QC|S11` (parent `D29|QC`)
- Tile / row / col: `D29` / 1 / 1
- Province: `QC`
- Centroid: 46.405203, -70.439037
- Allocated harvest: 121351.667265 m3
- Productive subcell area: 211721.019696 ha
- Committed geometry area: 229074.236452 ha
- Clipped inventory geometry: 229074.236452 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2244165
- Blocks: 827950
- Forest area: 201974.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73236
- Scheduled area: 17194.95 ha
- Eligible blocks (age class >= 40): 732352
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.77 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 28.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
