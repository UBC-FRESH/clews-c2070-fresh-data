# WS4 tiled 30-m dataset — L3|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L3|BC|S21` (parent `L3|BC`)
- Tile / row / col: `L3` / 2 / 1
- Province: `BC`
- Centroid: 55.814021, -129.796253
- Allocated harvest: 57984.589700 m3
- Productive subcell area: 105029.050119 ha
- Committed geometry area: 184311.313287 ha
- Clipped inventory geometry: 184311.313287 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 659362
- Blocks: 397696
- Forest area: 59342.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36928
- Scheduled area: 5295.33 ha
- Eligible blocks (age class >= 40): 369280
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.52 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 10.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
