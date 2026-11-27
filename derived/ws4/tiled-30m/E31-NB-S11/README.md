# WS4 tiled 30-m dataset — E31|NB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E31|NB|S11` (parent `E31|NB`)
- Tile / row / col: `E31` / 1 / 1
- Province: `NB`
- Centroid: 46.524470, -66.099615
- Allocated harvest: 181448.863957 m3
- Productive subcell area: 226598.170928 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2655484
- Blocks: 990574
- Forest area: 238993.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 78027
- Scheduled area: 14200.47 ha
- Eligible blocks (age class >= 40): 780264
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 32.39 MB
- Schedules: 0.93 MB
- Runs: 0.00 MB
- Total: 33.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
