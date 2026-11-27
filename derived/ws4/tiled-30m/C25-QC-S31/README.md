# WS4 tiled 30-m dataset — C25|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C25|QC|S31` (parent `C25|QC`)
- Tile / row / col: `C25` / 3 / 1
- Province: `QC`
- Centroid: 47.692272, -78.049158
- Allocated harvest: 117006.072005 m3
- Productive subcell area: 207249.434828 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2261357
- Blocks: 909984
- Forest area: 203522.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75124
- Scheduled area: 14238.72 ha
- Eligible blocks (age class >= 40): 751234
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.28 MB
- Schedules: 0.89 MB
- Runs: 0.00 MB
- Total: 30.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
