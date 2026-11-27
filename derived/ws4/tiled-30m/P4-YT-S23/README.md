# WS4 tiled 30-m dataset — P4|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P4|YT|S23` (parent `P4|YT`)
- Tile / row / col: `P4` / 2 / 3
- Province: `YT`
- Centroid: 61.729775, -131.841911
- Allocated harvest: 236.260843 m3
- Productive subcell area: 170296.639153 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2302881
- Blocks: 807291
- Forest area: 207259.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73232
- Scheduled area: 21181.68 ha
- Eligible blocks (age class >= 40): 732311
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.03 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 28.90 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
