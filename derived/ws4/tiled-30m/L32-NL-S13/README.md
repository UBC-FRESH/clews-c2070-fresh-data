# WS4 tiled 30-m dataset — L32|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L32|NL|S13` (parent `L32|NL`)
- Tile / row / col: `L32` / 1 / 3
- Province: `NL`
- Centroid: 53.468899, -55.883783
- Allocated harvest: 403.117524 m3
- Productive subcell area: 7192.520647 ha
- Committed geometry area: 13802.852999 ha
- Clipped inventory geometry: 13802.852999 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 14310
- Blocks: 11622
- Forest area: 1287.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 540
- Scheduled area: 56.34 ha
- Eligible blocks (age class >= 40): 5396
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.39 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
