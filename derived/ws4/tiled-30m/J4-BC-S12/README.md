# WS4 tiled 30-m dataset — J4|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J4|BC|S12` (parent `J4|BC`)
- Tile / row / col: `J4` / 1 / 2
- Province: `BC`
- Centroid: 53.906030, -124.430623
- Allocated harvest: 113986.006079 m3
- Productive subcell area: 218265.682259 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2252333
- Blocks: 835560
- Forest area: 202709.97 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73157
- Scheduled area: 13540.32 ha
- Eligible blocks (age class >= 40): 731568
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.34 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 28.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
