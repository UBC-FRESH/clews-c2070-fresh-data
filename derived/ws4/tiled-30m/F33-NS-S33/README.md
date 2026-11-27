# WS4 tiled 30-m dataset — F33|NS|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F33|NS|S33` (parent `F33|NS`)
- Tile / row / col: `F33` / 3 / 3
- Province: `NS`
- Centroid: 46.739023, -60.371050
- Allocated harvest: 2177.014720 m3
- Productive subcell area: 6524.404213 ha
- Committed geometry area: 7614.844278 ha
- Clipped inventory geometry: 7614.844278 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 75739
- Blocks: 23646
- Forest area: 6816.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2231
- Scheduled area: 549.81 ha
- Eligible blocks (age class >= 40): 22304
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.15 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
