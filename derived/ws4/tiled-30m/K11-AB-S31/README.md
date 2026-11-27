# WS4 tiled 30-m dataset — K11|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K11|AB|S31` (parent `K11|AB`)
- Tile / row / col: `K11` / 3 / 1
- Province: `AB`
- Centroid: 59.250111, -110.323029
- Allocated harvest: 21263.267620 m3
- Productive subcell area: 96640.166953 ha
- Committed geometry area: 182842.266036 ha
- Clipped inventory geometry: 182842.266036 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1097090
- Blocks: 163207
- Forest area: 98738.10 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9579
- Scheduled area: 2112.30 ha
- Eligible blocks (age class >= 40): 95789
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.31 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 9.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
