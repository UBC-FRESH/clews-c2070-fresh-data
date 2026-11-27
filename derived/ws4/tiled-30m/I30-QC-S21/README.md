# WS4 tiled 30-m dataset — I30|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I30|QC|S21` (parent `I30|QC`)
- Tile / row / col: `I30` / 2 / 1
- Province: `QC`
- Centroid: 52.280038, -63.967460
- Allocated harvest: 16191.088844 m3
- Productive subcell area: 71720.263520 ha
- Committed geometry area: 93691.374376 ha
- Clipped inventory geometry: 93691.374376 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 660976
- Blocks: 274299
- Forest area: 59487.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26040
- Scheduled area: 5769.81 ha
- Eligible blocks (age class >= 40): 260394
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.84 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 9.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
