# WS4 tiled 30-m dataset — F4|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F4|BC|S23` (parent `F4|BC`)
- Tile / row / col: `F4` / 2 / 3
- Province: `BC`
- Centroid: 49.559288, -120.407656
- Allocated harvest: 187932.035561 m3
- Productive subcell area: 186912.489401 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2437391
- Blocks: 960064
- Forest area: 219365.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 86147
- Scheduled area: 13770.54 ha
- Eligible blocks (age class >= 40): 861465
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.56 MB
- Schedules: 1.02 MB
- Runs: 0.00 MB
- Total: 31.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
