# WS4 tiled 30-m dataset — B27|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B27|QC|S33` (parent `B27|QC`)
- Tile / row / col: `B27` / 3 / 3
- Province: `QC`
- Centroid: 45.352998, -73.677151
- Allocated harvest: 30654.310067 m3
- Productive subcell area: 47297.918884 ha
- Committed geometry area: 217621.546077 ha
- Clipped inventory geometry: 217621.546077 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 599334
- Blocks: 218851
- Forest area: 53940.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13498
- Scheduled area: 2981.88 ha
- Eligible blocks (age class >= 40): 134975
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.83 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 7.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
