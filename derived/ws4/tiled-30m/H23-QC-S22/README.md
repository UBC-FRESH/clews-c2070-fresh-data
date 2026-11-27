# WS4 tiled 30-m dataset — H23|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H23|QC|S22` (parent `H23|QC`)
- Tile / row / col: `H23` / 2 / 2
- Province: `QC`
- Centroid: 54.398646, -78.936169
- Allocated harvest: 23701.518217 m3
- Productive subcell area: 128849.195098 ha
- Committed geometry area: 247933.600947 ha
- Clipped inventory geometry: 247933.600947 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1179593
- Blocks: 470754
- Forest area: 106163.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35642
- Scheduled area: 7253.91 ha
- Eligible blocks (age class >= 40): 356416
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.22 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 15.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
