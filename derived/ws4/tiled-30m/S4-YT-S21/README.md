# WS4 tiled 30-m dataset — S4|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S4|YT|S21` (parent `S4|YT`)
- Tile / row / col: `S4` / 2 / 1
- Province: `YT`
- Centroid: 64.536757, -138.949722
- Allocated harvest: 112.993599 m3
- Productive subcell area: 94174.546119 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 732824
- Blocks: 311645
- Forest area: 65954.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23721
- Scheduled area: 5015.16 ha
- Eligible blocks (age class >= 40): 237207
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.92 MB
- Schedules: 0.28 MB
- Runs: 0.00 MB
- Total: 10.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
