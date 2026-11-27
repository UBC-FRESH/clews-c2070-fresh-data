# WS4 tiled 30-m dataset — O3|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O3|YT|S23` (parent `O3|YT`)
- Tile / row / col: `O3` / 2 / 3
- Province: `YT`
- Centroid: 60.043284, -132.581524
- Allocated harvest: 52.897127 m3
- Productive subcell area: 17504.775326 ha
- Committed geometry area: 20892.846039 ha
- Clipped inventory geometry: 20892.846039 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 182862
- Blocks: 88868
- Forest area: 16457.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8709
- Scheduled area: 1727.91 ha
- Eligible blocks (age class >= 40): 87082
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.24 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 3.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
