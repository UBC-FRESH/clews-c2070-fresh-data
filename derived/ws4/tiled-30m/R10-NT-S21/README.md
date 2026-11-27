# WS4 tiled 30-m dataset — R10|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R10|NT|S21` (parent `R10|NT`)
- Tile / row / col: `R10` / 2 / 1
- Province: `NT`
- Centroid: 67.473572, -119.791905
- Allocated harvest: 0.396190 m3
- Productive subcell area: 1131.543184 ha
- Committed geometry area: 38652.704634 ha
- Clipped inventory geometry: 38652.704634 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 26814
- Blocks: 16728
- Forest area: 2413.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3205
- Scheduled area: 385.38 ha
- Eligible blocks (age class >= 40): 3205
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.58 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
