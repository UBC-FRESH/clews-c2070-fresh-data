# WS4 tiled 30-m dataset — E27|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E27|QC|S21` (parent `E27|QC`)
- Tile / row / col: `E27` / 2 / 1
- Province: `QC`
- Centroid: 49.025080, -73.186523
- Allocated harvest: 84414.444630 m3
- Productive subcell area: 198894.418245 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2488728
- Blocks: 818102
- Forest area: 223985.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65437
- Scheduled area: 14740.65 ha
- Eligible blocks (age class >= 40): 654370
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.56 MB
- Schedules: 0.78 MB
- Runs: 0.00 MB
- Total: 30.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
