# WS4 tiled 30-m dataset — S6|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S6|NT|S11` (parent `S6|NT`)
- Tile / row / col: `S6` / 1 / 1
- Province: `NT`
- Centroid: 65.974296, -132.849547
- Allocated harvest: 32.672279 m3
- Productive subcell area: 32012.063138 ha
- Committed geometry area: 56695.968268 ha
- Clipped inventory geometry: 56695.968268 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 509573
- Blocks: 157261
- Forest area: 45861.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11899
- Scheduled area: 2677.86 ha
- Eligible blocks (age class >= 40): 118990
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.27 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 6.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
