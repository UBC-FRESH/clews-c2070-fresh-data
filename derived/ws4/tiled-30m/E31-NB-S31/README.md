# WS4 tiled 30-m dataset — E31|NB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E31|NB|S31` (parent `E31|NB`)
- Tile / row / col: `E31` / 3 / 1
- Province: `NB`
- Centroid: 47.325453, -65.523771
- Allocated harvest: 180206.747737 m3
- Productive subcell area: 225046.983131 ha
- Committed geometry area: 248288.613948 ha
- Clipped inventory geometry: 248288.613948 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2580213
- Blocks: 862937
- Forest area: 232219.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 67241
- Scheduled area: 14931.81 ha
- Eligible blocks (age class >= 40): 672402
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.34 MB
- Schedules: 0.80 MB
- Runs: 0.00 MB
- Total: 31.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
