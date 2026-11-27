# WS4 tiled 30-m dataset — K9|AB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K9|AB|S13` (parent `K9|AB`)
- Tile / row / col: `K9` / 1 / 3
- Province: `AB`
- Centroid: 57.883727, -113.153501
- Allocated harvest: 136547.554935 m3
- Productive subcell area: 212379.340034 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2366414
- Blocks: 639473
- Forest area: 212977.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48005
- Scheduled area: 17800.65 ha
- Eligible blocks (age class >= 40): 480046
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.33 MB
- Schedules: 0.57 MB
- Runs: 0.00 MB
- Total: 25.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
