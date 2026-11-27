# WS4 tiled 30-m dataset — G17|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G17|MB|S11` (parent `G17|MB`)
- Tile / row / col: `G17` / 1 / 1
- Province: `MB`
- Centroid: 53.764948, -94.052230
- Allocated harvest: 5727.832177 m3
- Productive subcell area: 159950.548506 ha
- Committed geometry area: 216258.992670 ha
- Clipped inventory geometry: 216258.992670 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1571000
- Blocks: 515848
- Forest area: 141390.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44543
- Scheduled area: 8585.91 ha
- Eligible blocks (age class >= 40): 445423
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.22 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 18.74 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
