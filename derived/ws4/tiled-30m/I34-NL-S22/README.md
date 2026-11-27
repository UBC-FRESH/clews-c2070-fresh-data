# WS4 tiled 30-m dataset — I34|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I34|NL|S22` (parent `I34|NL`)
- Tile / row / col: `I34` / 2 / 2
- Province: `NL`
- Centroid: 49.257872, -55.954022
- Allocated harvest: 13412.972366 m3
- Productive subcell area: 174159.763710 ha
- Committed geometry area: 243601.797905 ha
- Clipped inventory geometry: 243601.797905 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2097747
- Blocks: 878952
- Forest area: 188797.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 78747
- Scheduled area: 15259.86 ha
- Eligible blocks (age class >= 40): 787466
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.98 MB
- Schedules: 0.93 MB
- Runs: 0.00 MB
- Total: 27.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
