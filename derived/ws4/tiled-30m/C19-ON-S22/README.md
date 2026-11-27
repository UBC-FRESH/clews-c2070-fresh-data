# WS4 tiled 30-m dataset — C19|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C19|ON|S22` (parent `C19|ON`)
- Tile / row / col: `C19` / 2 / 2
- Province: `ON`
- Centroid: 48.609101, -89.401435
- Allocated harvest: 48230.834165 m3
- Productive subcell area: 197634.298704 ha
- Committed geometry area: 236690.441417 ha
- Clipped inventory geometry: 236690.441417 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2185105
- Blocks: 791155
- Forest area: 196659.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69223
- Scheduled area: 15223.95 ha
- Eligible blocks (age class >= 40): 692230
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.74 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 27.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
