# WS4 tiled 30-m dataset — I34|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I34|NL|S21` (parent `I34|NL`)
- Tile / row / col: `I34` / 2 / 1
- Province: `NL`
- Centroid: 49.516387, -56.515730
- Allocated harvest: 13354.265406 m3
- Productive subcell area: 173397.487467 ha
- Committed geometry area: 242535.582268 ha
- Clipped inventory geometry: 242535.582268 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2112002
- Blocks: 933564
- Forest area: 190080.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 84709
- Scheduled area: 15034.77 ha
- Eligible blocks (age class >= 40): 847086
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.72 MB
- Schedules: 1.01 MB
- Runs: 0.00 MB
- Total: 28.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
