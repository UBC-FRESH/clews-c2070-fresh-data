# WS4 tiled 30-m dataset — F31|NB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F31|NB|S22` (parent `F31|NB`)
- Tile / row / col: `F31` / 2 / 2
- Province: `NB`
- Centroid: 47.871505, -64.584040
- Allocated harvest: 14631.568359 m3
- Productive subcell area: 16490.850734 ha
- Committed geometry area: 19884.707659 ha
- Clipped inventory geometry: 19884.707659 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 129312
- Blocks: 64684
- Forest area: 11638.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5012
- Scheduled area: 917.10 ha
- Eligible blocks (age class >= 40): 50114
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.37 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 2.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
