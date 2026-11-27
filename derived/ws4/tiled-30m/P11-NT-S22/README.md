# WS4 tiled 30-m dataset — P11|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P11|NT|S22` (parent `P11|NT`)
- Tile / row / col: `P11` / 2 / 2
- Province: `NT`
- Centroid: 65.514630, -113.067417
- Allocated harvest: 5.130235 m3
- Productive subcell area: 14469.909598 ha
- Committed geometry area: 81662.552877 ha
- Clipped inventory geometry: 81662.552877 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 29027
- Blocks: 21714
- Forest area: 2612.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 890
- Scheduled area: 90.54 ha
- Eligible blocks (age class >= 40): 8893
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.69 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
