# WS4 tiled 30-m dataset — P11|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P11|NT|S21` (parent `P11|NT`)
- Tile / row / col: `P11` / 2 / 1
- Province: `NT`
- Centroid: 65.495963, -113.895853
- Allocated harvest: 15.705479 m3
- Productive subcell area: 44297.551965 ha
- Committed geometry area: 249998.187986 ha
- Clipped inventory geometry: 249998.187986 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 541031
- Blocks: 283197
- Forest area: 48692.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17970
- Scheduled area: 2833.47 ha
- Eligible blocks (age class >= 40): 179694
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.28 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 8.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
