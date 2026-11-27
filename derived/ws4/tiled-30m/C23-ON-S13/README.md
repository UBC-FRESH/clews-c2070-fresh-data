# WS4 tiled 30-m dataset — C23|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C23|ON|S13` (parent `C23|ON`)
- Tile / row / col: `C23` / 1 / 3
- Province: `ON`
- Centroid: 47.256405, -80.926615
- Allocated harvest: 60746.402306 m3
- Productive subcell area: 219318.652196 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2489983
- Blocks: 882201
- Forest area: 224098.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 82231
- Scheduled area: 19468.08 ha
- Eligible blocks (age class >= 40): 822302
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.86 MB
- Schedules: 0.98 MB
- Runs: 0.00 MB
- Total: 31.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
