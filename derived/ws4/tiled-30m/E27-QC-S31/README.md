# WS4 tiled 30-m dataset — E27|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E27|QC|S31` (parent `E27|QC`)
- Tile / row / col: `E27` / 3 / 1
- Province: `QC`
- Centroid: 49.448591, -72.954259
- Allocated harvest: 84414.444630 m3
- Productive subcell area: 198894.418245 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2429911
- Blocks: 696967
- Forest area: 218691.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51595
- Scheduled area: 14509.62 ha
- Eligible blocks (age class >= 40): 515947
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.24 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 27.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
