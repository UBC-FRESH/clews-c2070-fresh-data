# WS4 tiled 30-m dataset — C28|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C28|QC|S23` (parent `C28|QC`)
- Tile / row / col: `C28` / 2 / 3
- Province: `QC`
- Centroid: 45.733551, -71.481259
- Allocated harvest: 73775.091185 m3
- Productive subcell area: 133755.670382 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2245152
- Blocks: 693718
- Forest area: 202063.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59445
- Scheduled area: 16782.03 ha
- Eligible blocks (age class >= 40): 594447
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.16 MB
- Schedules: 0.70 MB
- Runs: 0.00 MB
- Total: 26.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
