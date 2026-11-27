# WS4 tiled 30-m dataset — K23|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K23|QC|S22` (parent `K23|QC`)
- Tile / row / col: `K23` / 2 / 2
- Province: `QC`
- Centroid: 58.382212, -76.966879
- Allocated harvest: 1130.191881 m3
- Productive subcell area: 8354.649092 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 84596
- Blocks: 56960
- Forest area: 7613.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1017
- Scheduled area: 107.82 ha
- Eligible blocks (age class >= 40): 10170
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.78 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
