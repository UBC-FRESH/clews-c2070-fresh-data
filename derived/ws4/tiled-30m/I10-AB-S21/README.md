# WS4 tiled 30-m dataset — I10|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I10|AB|S21` (parent `I10|AB`)
- Tile / row / col: `I10` / 2 / 1
- Province: `AB`
- Centroid: 55.791835, -111.226221
- Allocated harvest: 82707.233931 m3
- Productive subcell area: 222888.722426 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2614687
- Blocks: 868988
- Forest area: 235321.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76373
- Scheduled area: 15998.76 ha
- Eligible blocks (age class >= 40): 763730
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.58 MB
- Schedules: 0.91 MB
- Runs: 0.00 MB
- Total: 31.48 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
