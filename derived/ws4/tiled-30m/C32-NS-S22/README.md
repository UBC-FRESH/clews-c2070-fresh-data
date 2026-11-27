# WS4 tiled 30-m dataset — C32|NS|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C32|NS|S22` (parent `C32|NS`)
- Tile / row / col: `C32` / 2 / 2
- Province: `NS`
- Centroid: 43.805722, -65.293864
- Allocated harvest: 88727.826790 m3
- Productive subcell area: 147745.288676 ha
- Committed geometry area: 177302.175025 ha
- Clipped inventory geometry: 177302.175025 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1622763
- Blocks: 539042
- Forest area: 146048.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48968
- Scheduled area: 13585.68 ha
- Eligible blocks (age class >= 40): 489678
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.74 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 20.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
