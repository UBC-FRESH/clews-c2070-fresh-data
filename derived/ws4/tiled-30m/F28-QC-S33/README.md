# WS4 tiled 30-m dataset — F28|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F28|QC|S33` (parent `F28|QC`)
- Tile / row / col: `F28` / 3 / 3
- Province: `QC`
- Centroid: 49.873729, -68.958580
- Allocated harvest: 76437.552511 m3
- Productive subcell area: 212220.092659 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2078705
- Blocks: 736279
- Forest area: 187083.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 61169
- Scheduled area: 13988.70 ha
- Eligible blocks (age class >= 40): 611686
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.42 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 26.15 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
