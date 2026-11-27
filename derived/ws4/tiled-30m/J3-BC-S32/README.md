# WS4 tiled 30-m dataset — J3|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J3|BC|S32` (parent `J3|BC`)
- Tile / row / col: `J3` / 3 / 2
- Province: `BC`
- Centroid: 54.076111, -127.210155
- Allocated harvest: 79991.178586 m3
- Productive subcell area: 186860.574082 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2412816
- Blocks: 896843
- Forest area: 217153.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81539
- Scheduled area: 14585.58 ha
- Eligible blocks (age class >= 40): 815388
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.55 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 30.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
