# WS4 tiled 30-m dataset — E30|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E30|QC|S32` (parent `E30|QC`)
- Tile / row / col: `E30` / 3 / 2
- Province: `QC`
- Centroid: 48.000934, -66.856714
- Allocated harvest: 236.248890 m3
- Productive subcell area: 389.788244 ha
- Committed geometry area: 422.382902 ha
- Clipped inventory geometry: 422.382902 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 3013
- Blocks: 1309
- Forest area: 271.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 976
- Scheduled area: 185.85 ha
- Eligible blocks (age class >= 40): 976
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.13 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
