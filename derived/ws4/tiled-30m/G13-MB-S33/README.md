# WS4 tiled 30-m dataset — G13|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G13|MB|S33` (parent `G13|MB`)
- Tile / row / col: `G13` / 3 / 3
- Province: `MB`
- Centroid: 54.454667, -101.646649
- Allocated harvest: 3325.942402 m3
- Productive subcell area: 70503.004540 ha
- Committed geometry area: 118282.165255 ha
- Clipped inventory geometry: 118282.165255 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 764458
- Blocks: 278250
- Forest area: 68801.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26003
- Scheduled area: 5939.46 ha
- Eligible blocks (age class >= 40): 260025
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.80 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 10.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
