# WS4 tiled 30-m dataset — J35|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J35|NL|S12` (parent `J35|NL`)
- Tile / row / col: `J35` / 1 / 2
- Province: `NL`
- Centroid: 49.185385, -53.710188
- Allocated harvest: 3792.889390 m3
- Productive subcell area: 54470.251361 ha
- Committed geometry area: 69684.292985 ha
- Clipped inventory geometry: 69684.292985 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 459835
- Blocks: 248434
- Forest area: 41385.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21964
- Scheduled area: 3746.16 ha
- Eligible blocks (age class >= 40): 219634
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.37 MB
- Schedules: 0.25 MB
- Runs: 0.00 MB
- Total: 7.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
