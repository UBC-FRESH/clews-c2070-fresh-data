# WS4 tiled 30-m dataset — I32|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I32|QC|S11` (parent `I32|QC`)
- Tile / row / col: `I32` / 1 / 1
- Province: `QC`
- Centroid: 50.613847, -60.433952
- Allocated harvest: 40999.595704 m3
- Productive subcell area: 175801.544324 ha
- Committed geometry area: 249660.741877 ha
- Clipped inventory geometry: 249660.741877 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2063483
- Blocks: 722289
- Forest area: 185713.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66429
- Scheduled area: 17200.17 ha
- Eligible blocks (age class >= 40): 664282
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.01 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 25.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
