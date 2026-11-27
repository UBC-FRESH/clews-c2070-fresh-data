# WS4 tiled 30-m dataset — E24|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E24|QC|S33` (parent `E24|QC`)
- Tile / row / col: `E24` / 3 / 3
- Province: `QC`
- Centroid: 50.412434, -77.613972
- Allocated harvest: 35482.439363 m3
- Productive subcell area: 174007.072475 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2118586
- Blocks: 667080
- Forest area: 190672.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 54802
- Scheduled area: 13981.32 ha
- Eligible blocks (age class >= 40): 548015
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.29 MB
- Schedules: 0.65 MB
- Runs: 0.00 MB
- Total: 24.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
