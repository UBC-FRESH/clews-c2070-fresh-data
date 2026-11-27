# WS4 tiled 30-m dataset — I29|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I29|QC|S23` (parent `I29|QC`)
- Tile / row / col: `I29` / 2 / 3
- Province: `QC`
- Centroid: 52.611816, -64.120124
- Allocated harvest: 1385.231214 m3
- Productive subcell area: 7602.427423 ha
- Committed geometry area: 11783.274600 ha
- Clipped inventory geometry: 11783.274600 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 110555
- Blocks: 30185
- Forest area: 9949.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2852
- Scheduled area: 759.69 ha
- Eligible blocks (age class >= 40): 28519
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.56 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
