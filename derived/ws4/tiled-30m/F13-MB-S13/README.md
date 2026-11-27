# WS4 tiled 30-m dataset — F13|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F13|MB|S13` (parent `F13|MB`)
- Tile / row / col: `F13` / 1 / 3
- Province: `MB`
- Centroid: 52.181703, -101.349562
- Allocated harvest: 6957.410242 m3
- Productive subcell area: 137859.018828 ha
- Committed geometry area: 178416.922707 ha
- Clipped inventory geometry: 178416.922707 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 657422
- Blocks: 172038
- Forest area: 59167.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15000
- Scheduled area: 5337.99 ha
- Eligible blocks (age class >= 40): 149994
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.42 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 7.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
