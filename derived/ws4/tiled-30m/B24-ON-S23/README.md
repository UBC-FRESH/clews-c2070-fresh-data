# WS4 tiled 30-m dataset — B24|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B24|ON|S23` (parent `B24|ON`)
- Tile / row / col: `B24` / 2 / 3
- Province: `ON`
- Centroid: 46.080080, -79.337848
- Allocated harvest: 68244.312992 m3
- Productive subcell area: 257021.272469 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2133211
- Blocks: 648151
- Forest area: 191988.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59968
- Scheduled area: 17097.93 ha
- Eligible blocks (age class >= 40): 599676
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.64 MB
- Schedules: 0.71 MB
- Runs: 0.00 MB
- Total: 25.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
