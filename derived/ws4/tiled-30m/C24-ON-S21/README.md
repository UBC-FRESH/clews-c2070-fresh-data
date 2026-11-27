# WS4 tiled 30-m dataset — C24|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C24|ON|S21` (parent `C24|ON`)
- Tile / row / col: `C24` / 2 / 1
- Province: `ON`
- Centroid: 47.590989, -80.136637
- Allocated harvest: 57880.838078 m3
- Productive subcell area: 204933.639514 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2143022
- Blocks: 765350
- Forest area: 192871.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 64536
- Scheduled area: 13413.78 ha
- Eligible blocks (age class >= 40): 645359
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.12 MB
- Schedules: 0.77 MB
- Runs: 0.00 MB
- Total: 26.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
