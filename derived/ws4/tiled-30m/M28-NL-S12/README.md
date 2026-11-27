# WS4 tiled 30-m dataset — M28|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M28|NL|S12` (parent `M28|NL`)
- Tile / row / col: `M28` / 1 / 2
- Province: `NL`
- Centroid: 57.866176, -63.210087
- Allocated harvest: 860.773973 m3
- Productive subcell area: 10040.756049 ha
- Committed geometry area: 242962.758585 ha
- Clipped inventory geometry: 242962.758585 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 98468
- Blocks: 50505
- Forest area: 8862.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2702
- Scheduled area: 480.15 ha
- Eligible blocks (age class >= 40): 27019
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.82 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
