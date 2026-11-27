# WS4 tiled 30-m dataset — I34|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I34|NL|S31` (parent `I34|NL`)
- Tile / row / col: `I34` / 3 / 1
- Province: `NL`
- Centroid: 49.862990, -56.127767
- Allocated harvest: 10356.928718 m3
- Productive subcell area: 134478.787332 ha
- Committed geometry area: 188098.982660 ha
- Clipped inventory geometry: 188098.982660 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1715537
- Blocks: 832145
- Forest area: 154398.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76503
- Scheduled area: 13477.59 ha
- Eligible blocks (age class >= 40): 765026
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.58 MB
- Schedules: 0.91 MB
- Runs: 0.00 MB
- Total: 24.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
