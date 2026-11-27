# WS4 tiled 30-m dataset — G31|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G31|QC|S23` (parent `G31|QC`)
- Tile / row / col: `G31` / 2 / 3
- Province: `QC`
- Centroid: 49.191266, -62.911377
- Allocated harvest: 10.652400 m3
- Productive subcell area: 23.725479 ha
- Committed geometry area: 27.847262 ha
- Clipped inventory geometry: 27.847262 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 185
- Blocks: 111
- Forest area: 16.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 103
- Scheduled area: 15.93 ha
- Eligible blocks (age class >= 40): 103
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
