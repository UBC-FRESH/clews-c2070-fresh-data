# WS4 tiled 30-m dataset — H27|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H27|QC|S12` (parent `H27|QC`)
- Tile / row / col: `H27` / 1 / 2
- Province: `QC`
- Centroid: 52.244849, -70.496647
- Allocated harvest: 24638.467147 m3
- Productive subcell area: 154824.167230 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2148298
- Blocks: 354340
- Forest area: 193346.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30770
- Scheduled area: 33181.65 ha
- Eligible blocks (age class >= 40): 307694
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.53 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 19.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
