# WS4 tiled 30-m dataset — I28|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I28|QC|S12` (parent `I28|QC`)
- Tile / row / col: `I28` / 1 / 2
- Province: `QC`
- Centroid: 52.944309, -67.612088
- Allocated harvest: 18853.665862 m3
- Productive subcell area: 122840.569632 ha
- Committed geometry area: 207462.786999 ha
- Clipped inventory geometry: 207462.786999 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1140176
- Blocks: 440484
- Forest area: 102615.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 34744
- Scheduled area: 8801.37 ha
- Eligible blocks (age class >= 40): 347432
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.40 MB
- Schedules: 0.41 MB
- Runs: 0.00 MB
- Total: 14.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
