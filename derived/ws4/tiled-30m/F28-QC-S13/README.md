# WS4 tiled 30-m dataset — F28|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F28|QC|S13` (parent `F28|QC`)
- Tile / row / col: `F28` / 1 / 3
- Province: `QC`
- Centroid: 49.045928, -69.503212
- Allocated harvest: 76437.552511 m3
- Productive subcell area: 212220.092659 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2363545
- Blocks: 812804
- Forest area: 212719.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68917
- Scheduled area: 15766.38 ha
- Eligible blocks (age class >= 40): 689166
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.39 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 29.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
