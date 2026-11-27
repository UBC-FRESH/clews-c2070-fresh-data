# WS4 tiled 30-m dataset — J24|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J24|QC|S12` (parent `J24|QC`)
- Tile / row / col: `J24` / 1 / 2
- Province: `QC`
- Centroid: 56.220716, -75.515665
- Allocated harvest: 10709.596663 m3
- Productive subcell area: 64489.195964 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1216998
- Blocks: 599448
- Forest area: 109529.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43468
- Scheduled area: 8174.34 ha
- Eligible blocks (age class >= 40): 434675
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.99 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 17.51 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
