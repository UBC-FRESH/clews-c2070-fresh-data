# WS4 tiled 30-m dataset — J33|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J33|NL|S31` (parent `J33|NL`)
- Tile / row / col: `J33` / 3 / 1
- Province: `NL`
- Centroid: 51.817484, -56.690556
- Allocated harvest: 6348.332520 m3
- Productive subcell area: 134112.550992 ha
- Committed geometry area: 202105.328574 ha
- Clipped inventory geometry: 202105.328574 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1269589
- Blocks: 625704
- Forest area: 114263.01 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51700
- Scheduled area: 9640.08 ha
- Eligible blocks (age class >= 40): 516998
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.22 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 18.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
