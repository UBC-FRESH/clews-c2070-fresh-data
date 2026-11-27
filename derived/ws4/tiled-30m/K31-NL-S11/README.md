# WS4 tiled 30-m dataset — K31|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K31|NL|S11` (parent `K31|NL`)
- Tile / row / col: `K31` / 1 / 1
- Province: `NL`
- Centroid: 53.663394, -60.158147
- Allocated harvest: 6310.985412 m3
- Productive subcell area: 100728.896686 ha
- Committed geometry area: 134790.358495 ha
- Clipped inventory geometry: 134790.358495 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1192682
- Blocks: 329756
- Forest area: 107341.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31559
- Scheduled area: 9176.94 ha
- Eligible blocks (age class >= 40): 315582
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.44 MB
- Schedules: 0.37 MB
- Runs: 0.00 MB
- Total: 13.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
