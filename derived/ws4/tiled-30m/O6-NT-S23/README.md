# WS4 tiled 30-m dataset — O6|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O6|NT|S23` (parent `O6|NT`)
- Tile / row / col: `O6` / 2 / 3
- Province: `NT`
- Centroid: 61.928681, -125.292072
- Allocated harvest: 101.797925 m3
- Productive subcell area: 122838.100117 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 995522
- Blocks: 506723
- Forest area: 89596.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42438
- Scheduled area: 7377.48 ha
- Eligible blocks (age class >= 40): 424378
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.28 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 14.78 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
