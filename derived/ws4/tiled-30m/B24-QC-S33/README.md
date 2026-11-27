# WS4 tiled 30-m dataset — B24|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B24|QC|S33` (parent `B24|QC`)
- Tile / row / col: `B24` / 3 / 3
- Province: `QC`
- Centroid: 46.612099, -78.928475
- Allocated harvest: 16184.927162 m3
- Productive subcell area: 31124.204488 ha
- Committed geometry area: 36596.545033 ha
- Clipped inventory geometry: 36596.545033 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 325988
- Blocks: 111225
- Forest area: 29338.92 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10734
- Scheduled area: 2772.63 ha
- Eligible blocks (age class >= 40): 107336
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.65 MB
- Schedules: 0.12 MB
- Runs: 0.00 MB
- Total: 4.77 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
