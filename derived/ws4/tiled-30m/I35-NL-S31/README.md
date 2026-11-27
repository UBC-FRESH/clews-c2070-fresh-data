# WS4 tiled 30-m dataset — I35|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I35|NL|S31` (parent `I35|NL`)
- Tile / row / col: `I35` / 3 / 1
- Province: `NL`
- Centroid: 49.096427, -54.439413
- Allocated harvest: 12191.691982 m3
- Productive subcell area: 159821.482305 ha
- Committed geometry area: 245484.647748 ha
- Clipped inventory geometry: 245484.647748 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1974980
- Blocks: 842708
- Forest area: 177748.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74209
- Scheduled area: 13523.76 ha
- Eligible blocks (age class >= 40): 742083
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.75 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 26.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
