# WS4 tiled 30-m dataset — J7|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J7|AB|S23` (parent `J7|AB`)
- Tile / row / col: `J7` / 2 / 3
- Province: `AB`
- Centroid: 56.144701, -117.426866
- Allocated harvest: 68788.071280 m3
- Productive subcell area: 127335.026705 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 974299
- Blocks: 319583
- Forest area: 87686.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27070
- Scheduled area: 7259.13 ha
- Eligible blocks (age class >= 40): 270700
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.69 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 12.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
