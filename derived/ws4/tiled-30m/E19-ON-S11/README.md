# WS4 tiled 30-m dataset — E19|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E19|ON|S11` (parent `E19|ON`)
- Tile / row / col: `E19` / 1 / 1
- Province: `ON`
- Centroid: 50.883050, -89.784728
- Allocated harvest: 41545.087168 m3
- Productive subcell area: 202173.746580 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2180658
- Blocks: 664649
- Forest area: 196259.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57913
- Scheduled area: 14798.34 ha
- Eligible blocks (age class >= 40): 579126
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.98 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 25.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
