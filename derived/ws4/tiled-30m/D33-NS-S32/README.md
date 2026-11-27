# WS4 tiled 30-m dataset — D33|NS|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D33|NS|S32` (parent `D33|NS`)
- Tile / row / col: `D33` / 3 / 2
- Province: `NS`
- Centroid: 44.879328, -62.578580
- Allocated harvest: 12544.171500 m3
- Productive subcell area: 26044.390070 ha
- Committed geometry area: 31532.344458 ha
- Clipped inventory geometry: 31532.344458 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 306497
- Blocks: 98723
- Forest area: 27584.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8239
- Scheduled area: 1835.28 ha
- Eligible blocks (age class >= 40): 82386
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.17 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 4.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
