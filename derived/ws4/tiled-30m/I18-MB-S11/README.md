# WS4 tiled 30-m dataset — I18|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I18|MB|S11` (parent `I18|MB`)
- Tile / row / col: `I18` / 1 / 1
- Province: `MB`
- Centroid: 56.438576, -91.448726
- Allocated harvest: 1740.777450 m3
- Productive subcell area: 134512.346602 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1379893
- Blocks: 522104
- Forest area: 124190.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41566
- Scheduled area: 9811.89 ha
- Eligible blocks (age class >= 40): 415651
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.18 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 17.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
