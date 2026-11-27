# WS4 tiled 30-m dataset — D16|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D16|MB|S22` (parent `D16|MB`)
- Tile / row / col: `D16` / 2 / 2
- Province: `MB`
- Centroid: 50.112821, -95.504187
- Allocated harvest: 9235.687967 m3
- Productive subcell area: 176278.567546 ha
- Committed geometry area: 249976.200225 ha
- Clipped inventory geometry: 249976.200225 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1995685
- Blocks: 943419
- Forest area: 179611.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 89188
- Scheduled area: 16655.85 ha
- Eligible blocks (age class >= 40): 891874
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.23 MB
- Schedules: 1.06 MB
- Runs: 0.00 MB
- Total: 28.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
