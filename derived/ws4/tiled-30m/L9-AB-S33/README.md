# WS4 tiled 30-m dataset — L9|AB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L9|AB|S33` (parent `L9|AB`)
- Tile / row / col: `L9` / 3 / 3
- Province: `AB`
- Centroid: 59.928841, -114.438759
- Allocated harvest: 29243.516035 m3
- Productive subcell area: 58548.800582 ha
- Committed geometry area: 74581.560092 ha
- Clipped inventory geometry: 74581.560092 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 624597
- Blocks: 237772
- Forest area: 56213.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19062
- Scheduled area: 3435.93 ha
- Eligible blocks (age class >= 40): 190613
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.21 MB
- Schedules: 0.22 MB
- Runs: 0.00 MB
- Total: 8.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
