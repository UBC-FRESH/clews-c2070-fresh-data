# WS4 tiled 30-m dataset — H35|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H35|NL|S33` (parent `H35|NL`)
- Tile / row / col: `H35` / 3 / 3
- Province: `NL`
- Centroid: 47.544291, -54.616622
- Allocated harvest: 5360.571327 m3
- Productive subcell area: 72313.905165 ha
- Committed geometry area: 150980.971216 ha
- Clipped inventory geometry: 150980.971216 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1069844
- Blocks: 564267
- Forest area: 96285.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49835
- Scheduled area: 8743.41 ha
- Eligible blocks (age class >= 40): 498341
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.52 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 16.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
