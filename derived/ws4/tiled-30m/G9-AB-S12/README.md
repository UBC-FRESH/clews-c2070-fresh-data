# WS4 tiled 30-m dataset — G9|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G9|AB|S12` (parent `G9|AB`)
- Tile / row / col: `G9` / 1 / 2
- Province: `AB`
- Centroid: 52.467147, -111.351953
- Allocated harvest: 5046.451848 m3
- Productive subcell area: 12852.811668 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 531293
- Blocks: 209399
- Forest area: 47816.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9354
- Scheduled area: 2976.84 ha
- Eligible blocks (age class >= 40): 93532
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.14 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 7.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
