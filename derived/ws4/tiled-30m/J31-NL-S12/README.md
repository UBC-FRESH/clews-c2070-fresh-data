# WS4 tiled 30-m dataset — J31|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J31|NL|S12` (parent `J31|NL`)
- Tile / row / col: `J31` / 1 / 2
- Province: `NL`
- Centroid: 52.252191, -60.554652
- Allocated harvest: 14584.425099 m3
- Productive subcell area: 203451.770580 ha
- Committed geometry area: 244705.126652 ha
- Clipped inventory geometry: 244705.126652 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2309360
- Blocks: 723482
- Forest area: 207842.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69946
- Scheduled area: 19915.11 ha
- Eligible blocks (age class >= 40): 699458
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.01 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 27.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
