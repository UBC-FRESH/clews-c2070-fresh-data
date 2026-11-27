# WS4 tiled 30-m dataset — C19|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C19|ON|S33` (parent `C19|ON`)
- Tile / row / col: `C19` / 3 / 3
- Province: `ON`
- Centroid: 49.013052, -88.656051
- Allocated harvest: 48794.011137 m3
- Productive subcell area: 199942.015079 ha
- Committed geometry area: 239454.204646 ha
- Clipped inventory geometry: 239454.204646 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2397447
- Blocks: 718678
- Forest area: 215770.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62969
- Scheduled area: 17084.34 ha
- Eligible blocks (age class >= 40): 629688
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.41 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 28.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
