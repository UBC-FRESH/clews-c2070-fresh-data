# WS4 tiled 30-m dataset — M27|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M27|QC|S12` (parent `M27|QC`)
- Tile / row / col: `M27` / 1 / 2
- Province: `QC`
- Centroid: 58.510656, -65.527662
- Allocated harvest: 3573.867808 m3
- Productive subcell area: 19509.725801 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 382593
- Blocks: 207666
- Forest area: 34433.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15254
- Scheduled area: 2578.23 ha
- Eligible blocks (age class >= 40): 152533
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.28 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 6.45 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
