# WS4 tiled 30-m dataset — R4|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R4|YT|S32` (parent `R4|YT`)
- Tile / row / col: `R4` / 3 / 2
- Province: `YT`
- Centroid: 64.102449, -136.785688
- Allocated harvest: 337.589146 m3
- Productive subcell area: 176424.897866 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1336265
- Blocks: 504228
- Forest area: 120263.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36518
- Scheduled area: 8329.41 ha
- Eligible blocks (age class >= 40): 365179
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.85 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 17.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
