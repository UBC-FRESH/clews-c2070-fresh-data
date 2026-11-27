# WS4 tiled 30-m dataset — E32|NS|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|NS|S22` (parent `E32|NS`)
- Tile / row / col: `E32` / 2 / 2
- Province: `NS`
- Centroid: 45.857639, -63.479204
- Allocated harvest: 1307.999587 m3
- Productive subcell area: 2789.566454 ha
- Committed geometry area: 3447.675298 ha
- Clipped inventory geometry: 3447.675298 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 20352
- Blocks: 8470
- Forest area: 1831.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 576
- Scheduled area: 112.05 ha
- Eligible blocks (age class >= 40): 5759
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.40 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
