# WS4 tiled 30-m dataset — I11|SK|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I11|SK|S12` (parent `I11|SK`)
- Tile / row / col: `I11` / 1 / 2
- Province: `SK`
- Centroid: 55.761109, -107.871469
- Allocated harvest: 28220.710290 m3
- Productive subcell area: 170588.489849 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1461449
- Blocks: 450949
- Forest area: 131530.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28345
- Scheduled area: 5480.46 ha
- Eligible blocks (age class >= 40): 283446
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.72 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 17.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
