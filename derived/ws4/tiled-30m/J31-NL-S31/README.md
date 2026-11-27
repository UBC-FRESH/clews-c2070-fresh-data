# WS4 tiled 30-m dataset — J31|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J31|NL|S31` (parent `J31|NL`)
- Tile / row / col: `J31` / 3 / 1
- Province: `NL`
- Centroid: 53.253047, -60.435259
- Allocated harvest: 13996.569450 m3
- Productive subcell area: 195251.222955 ha
- Committed geometry area: 234841.776535 ha
- Clipped inventory geometry: 234841.776535 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2144813
- Blocks: 850995
- Forest area: 193033.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81682
- Scheduled area: 18199.53 ha
- Eligible blocks (age class >= 40): 816812
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.29 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 28.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
