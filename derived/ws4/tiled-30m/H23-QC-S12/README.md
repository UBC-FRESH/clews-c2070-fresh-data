# WS4 tiled 30-m dataset — H23|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H23|QC|S12` (parent `H23|QC`)
- Tile / row / col: `H23` / 1 / 2
- Province: `QC`
- Centroid: 53.968071, -78.935863
- Allocated harvest: 10684.680490 m3
- Productive subcell area: 58085.413280 ha
- Committed geometry area: 111768.844703 ha
- Clipped inventory geometry: 111768.844703 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 908945
- Blocks: 402663
- Forest area: 81805.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 34892
- Scheduled area: 7268.31 ha
- Eligible blocks (age class >= 40): 348912
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.29 MB
- Schedules: 0.41 MB
- Runs: 0.00 MB
- Total: 12.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
