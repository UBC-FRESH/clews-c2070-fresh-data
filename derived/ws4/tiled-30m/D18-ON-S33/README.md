# WS4 tiled 30-m dataset — D18|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D18|ON|S33` (parent `D18|ON`)
- Tile / row / col: `D18` / 3 / 3
- Province: `ON`
- Centroid: 50.466429, -90.548428
- Allocated harvest: 47213.649233 m3
- Productive subcell area: 198941.060588 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2165298
- Blocks: 675227
- Forest area: 194876.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62177
- Scheduled area: 18199.71 ha
- Eligible blocks (age class >= 40): 621766
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.02 MB
- Schedules: 0.74 MB
- Runs: 0.00 MB
- Total: 25.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
