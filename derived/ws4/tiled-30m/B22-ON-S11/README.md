# WS4 tiled 30-m dataset — B22|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B22|ON|S11` (parent `B22|ON`)
- Tile / row / col: `B22` / 1 / 1
- Province: `ON`
- Centroid: 46.544274, -84.408224
- Allocated harvest: 7614.734376 m3
- Productive subcell area: 25994.784744 ha
- Committed geometry area: 28878.864942 ha
- Clipped inventory geometry: 28878.864942 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 219515
- Blocks: 63483
- Forest area: 19756.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5471
- Scheduled area: 2186.55 ha
- Eligible blocks (age class >= 40): 54709
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.94 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
