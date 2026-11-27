# WS4 tiled 30-m dataset — F16|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F16|MB|S22` (parent `F16|MB`)
- Tile / row / col: `F16` / 2 / 2
- Province: `MB`
- Centroid: 52.833035, -95.539903
- Allocated harvest: 7549.432927 m3
- Productive subcell area: 204111.368633 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1982377
- Blocks: 615160
- Forest area: 178413.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49001
- Scheduled area: 10809.27 ha
- Eligible blocks (age class >= 40): 490008
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.50 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 23.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
