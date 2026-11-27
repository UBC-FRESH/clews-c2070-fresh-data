# WS4 tiled 30-m dataset — L27|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L27|QC|S11` (parent `L27|QC`)
- Tile / row / col: `L27` / 1 / 1
- Province: `QC`
- Centroid: 57.465255, -67.436578
- Allocated harvest: 14919.959864 m3
- Productive subcell area: 91923.631808 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1892421
- Blocks: 1016727
- Forest area: 170317.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 90216
- Scheduled area: 13990.05 ha
- Eligible blocks (age class >= 40): 902153
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.83 MB
- Schedules: 1.07 MB
- Runs: 0.00 MB
- Total: 27.90 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
