# WS4 tiled 30-m dataset — H13|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H13|SK|S13` (parent `H13|SK`)
- Tile / row / col: `H13` / 1 / 3
- Province: `SK`
- Centroid: 54.892411, -102.106483
- Allocated harvest: 18900.375050 m3
- Productive subcell area: 103499.561827 ha
- Committed geometry area: 143433.994896 ha
- Clipped inventory geometry: 143433.994896 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 451084
- Blocks: 124963
- Forest area: 40597.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7352
- Scheduled area: 1120.23 ha
- Eligible blocks (age class >= 40): 73513
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.44 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 5.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
