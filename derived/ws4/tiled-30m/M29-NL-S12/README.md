# WS4 tiled 30-m dataset — M29|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M29|NL|S12` (parent `M29|NL`)
- Tile / row / col: `M29` / 1 / 2
- Province: `NL`
- Centroid: 57.113037, -61.448352
- Allocated harvest: 264.665209 m3
- Productive subcell area: 3061.709722 ha
- Committed geometry area: 8083.475982 ha
- Clipped inventory geometry: 8083.475982 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 3084
- Blocks: 2040
- Forest area: 277.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 989
- Scheduled area: 138.06 ha
- Eligible blocks (age class >= 40): 989
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.12 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
