# WS4 tiled 30-m dataset — S6|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S6|YT|S31` (parent `S6|YT`)
- Tile / row / col: `S6` / 3 / 1
- Province: `YT`
- Centroid: 66.594373, -134.331530
- Allocated harvest: 306.888770 m3
- Productive subcell area: 168468.202311 ha
- Committed geometry area: 243267.035367 ha
- Clipped inventory geometry: 243267.035367 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1874239
- Blocks: 568953
- Forest area: 168681.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43312
- Scheduled area: 9464.31 ha
- Eligible blocks (age class >= 40): 433113
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.87 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 21.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
