# WS4 tiled 30-m dataset — M7|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|NT|S31` (parent `M7|NT`)
- Tile / row / col: `M7` / 3 / 1
- Province: `NT`
- Centroid: 60.137630, -122.369341
- Allocated harvest: 167.689496 m3
- Productive subcell area: 106567.806708 ha
- Committed geometry area: 156339.662791 ha
- Clipped inventory geometry: 156339.662791 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 974619
- Blocks: 434407
- Forest area: 87715.71 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42120
- Scheduled area: 8447.31 ha
- Eligible blocks (age class >= 40): 421193
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.31 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 13.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
