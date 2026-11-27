# WS4 tiled 30-m dataset — K32|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K32|NL|S31` (parent `K32|NL`)
- Tile / row / col: `K32` / 3 / 1
- Province: `NL`
- Centroid: 53.743780, -57.422014
- Allocated harvest: 8392.668043 m3
- Productive subcell area: 153004.888379 ha
- Committed geometry area: 191521.386489 ha
- Clipped inventory geometry: 191521.386489 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1769176
- Blocks: 576908
- Forest area: 159225.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52714
- Scheduled area: 12327.66 ha
- Eligible blocks (age class >= 40): 527132
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.78 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 21.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
