# WS4 tiled 30-m dataset — K29|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K29|NL|S21` (parent `K29|NL`)
- Tile / row / col: `K29` / 2 / 1
- Province: `NL`
- Centroid: 55.445740, -63.492199
- Allocated harvest: 1768.938642 m3
- Productive subcell area: 36964.388711 ha
- Committed geometry area: 78487.868722 ha
- Clipped inventory geometry: 78487.868722 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 330229
- Blocks: 182053
- Forest area: 29720.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13084
- Scheduled area: 1874.25 ha
- Eligible blocks (age class >= 40): 130838
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.53 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 5.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
