# WS4 tiled 30-m dataset — J3|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J3|BC|S13` (parent `J3|BC`)
- Tile / row / col: `J3` / 1 / 3
- Province: `BC`
- Centroid: 53.489855, -125.799406
- Allocated harvest: 79991.178586 m3
- Productive subcell area: 186860.574082 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2362047
- Blocks: 420785
- Forest area: 212584.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33539
- Scheduled area: 6064.74 ha
- Eligible blocks (age class >= 40): 335385
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.41 MB
- Schedules: 0.39 MB
- Runs: 0.00 MB
- Total: 20.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
