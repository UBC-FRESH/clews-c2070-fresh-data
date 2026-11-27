# WS4 tiled 30-m dataset — V6|YT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `V6|YT|S22` (parent `V6|YT`)
- Tile / row / col: `V6` / 2 / 2
- Province: `YT`
- Centroid: 69.602001, -139.147807
- Allocated harvest: 0.527775 m3
- Productive subcell area: 457.135088 ha
- Committed geometry area: 10488.455835 ha
- Clipped inventory geometry: 10488.455835 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 52
- Blocks: 46
- Forest area: 4.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1
- Scheduled area: 0.09 ha
- Eligible blocks (age class >= 40): 1
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.07 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
