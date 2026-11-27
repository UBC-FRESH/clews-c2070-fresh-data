# WS4 tiled 30-m dataset — J27|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J27|QC|S23` (parent `J27|QC`)
- Tile / row / col: `J27` / 2 / 3
- Province: `QC`
- Centroid: 54.995565, -67.690379
- Allocated harvest: 16525.417418 m3
- Productive subcell area: 136090.334258 ha
- Committed geometry area: 230596.736661 ha
- Clipped inventory geometry: 230596.736661 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1604926
- Blocks: 886553
- Forest area: 144443.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 78044
- Scheduled area: 12541.23 ha
- Eligible blocks (age class >= 40): 780438
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.39 MB
- Schedules: 0.93 MB
- Runs: 0.00 MB
- Total: 24.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
