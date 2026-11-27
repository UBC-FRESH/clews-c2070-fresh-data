# WS4 tiled 30-m dataset — L30|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L30|NL|S21` (parent `L30|NL`)
- Tile / row / col: `L30` / 2 / 1
- Province: `NL`
- Centroid: 55.746759, -60.450861
- Allocated harvest: 1170.716240 m3
- Productive subcell area: 17127.268710 ha
- Committed geometry area: 35289.198349 ha
- Clipped inventory geometry: 35289.198349 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 164810
- Blocks: 62624
- Forest area: 14832.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3926
- Scheduled area: 1377.45 ha
- Eligible blocks (age class >= 40): 39255
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.51 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 2.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
