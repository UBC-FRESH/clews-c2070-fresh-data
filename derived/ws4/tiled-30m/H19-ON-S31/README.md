# WS4 tiled 30-m dataset — H19|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H19|ON|S31` (parent `H19|ON`)
- Tile / row / col: `H19` / 3 / 1
- Province: `ON`
- Centroid: 55.878051, -89.049590
- Allocated harvest: 6338.191285 m3
- Productive subcell area: 115530.030253 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1306772
- Blocks: 523513
- Forest area: 117609.48 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36505
- Scheduled area: 9272.52 ha
- Eligible blocks (age class >= 40): 365045
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.79 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 17.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
