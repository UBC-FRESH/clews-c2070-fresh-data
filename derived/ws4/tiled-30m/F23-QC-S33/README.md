# WS4 tiled 30-m dataset — F23|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F23|QC|S33` (parent `F23|QC`)
- Tile / row / col: `F23` / 3 / 3
- Province: `QC`
- Centroid: 51.913158, -78.858019
- Allocated harvest: 179.408640 m3
- Productive subcell area: 1411.765269 ha
- Committed geometry area: 2132.554675 ha
- Clipped inventory geometry: 2132.554675 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 14428
- Blocks: 7165
- Forest area: 1298.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 645
- Scheduled area: 119.43 ha
- Eligible blocks (age class >= 40): 6444
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.31 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
