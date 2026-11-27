# WS4 tiled 30-m dataset — H34|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H34|NL|S13` (parent `H34|NL`)
- Tile / row / col: `H34` / 1 / 3
- Province: `NL`
- Centroid: 47.670404, -56.931189
- Allocated harvest: 2654.738801 m3
- Productive subcell area: 43800.969590 ha
- Committed geometry area: 86944.127023 ha
- Clipped inventory geometry: 86944.127023 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 371486
- Blocks: 240289
- Forest area: 33433.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19091
- Scheduled area: 2668.95 ha
- Eligible blocks (age class >= 40): 190905
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.64 MB
- Schedules: 0.22 MB
- Runs: 0.00 MB
- Total: 6.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
