# WS4 tiled 30-m dataset — L25|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L25|QC|S33` (parent `L25|QC`)
- Tile / row / col: `L25` / 3 / 3
- Province: `QC`
- Centroid: 59.065249, -69.967350
- Allocated harvest: 797.717567 m3
- Productive subcell area: 6115.365937 ha
- Committed geometry area: 219534.489250 ha
- Clipped inventory geometry: 219534.489250 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 5576
- Blocks: 4827
- Forest area: 501.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 577
- Scheduled area: 55.62 ha
- Eligible blocks (age class >= 40): 577
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.19 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
