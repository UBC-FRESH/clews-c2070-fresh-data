# WS4 tiled 30-m dataset — L11|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L11|NT|S13` (parent `L11|NT`)
- Tile / row / col: `L11` / 1 / 3
- Province: `NT`
- Centroid: 60.070683, -108.646375
- Allocated harvest: 31.732961 m3
- Productive subcell area: 44764.419220 ha
- Committed geometry area: 74515.097814 ha
- Clipped inventory geometry: 74515.097814 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 667691
- Blocks: 84218
- Forest area: 60092.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4972
- Scheduled area: 1392.03 ha
- Eligible blocks (age class >= 40): 49712
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.61 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 5.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
