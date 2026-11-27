# WS4 tiled 30-m dataset — E24|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E24|QC|S31` (parent `E24|QC`)
- Tile / row / col: `E24` / 3 / 1
- Province: `QC`
- Centroid: 50.647112, -78.983735
- Allocated harvest: 35482.439363 m3
- Productive subcell area: 174007.072475 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1725445
- Blocks: 629783
- Forest area: 155290.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53217
- Scheduled area: 12228.30 ha
- Eligible blocks (age class >= 40): 532165
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.73 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 21.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
