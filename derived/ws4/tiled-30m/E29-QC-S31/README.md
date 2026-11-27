# WS4 tiled 30-m dataset — E29|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E29|QC|S31` (parent `E29|QC`)
- Tile / row / col: `E29` / 3 / 1
- Province: `QC`
- Centroid: 48.497460, -69.293239
- Allocated harvest: 43263.799879 m3
- Productive subcell area: 74390.407306 ha
- Committed geometry area: 90262.868444 ha
- Clipped inventory geometry: 90262.868444 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 831107
- Blocks: 336342
- Forest area: 74799.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28578
- Scheduled area: 5645.79 ha
- Eligible blocks (age class >= 40): 285772
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.94 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 11.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
