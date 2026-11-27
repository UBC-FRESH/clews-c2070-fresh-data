# WS4 tiled 30-m dataset — L13|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L13|NT|S11` (parent `L13|NT`)
- Tile / row / col: `L13` / 1 / 1
- Province: `NT`
- Centroid: 60.251438, -104.999185
- Allocated harvest: 40.589939 m3
- Productive subcell area: 104358.579820 ha
- Committed geometry area: 249245.969237 ha
- Clipped inventory geometry: 249245.969237 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1442979
- Blocks: 463979
- Forest area: 129868.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39376
- Scheduled area: 8270.37 ha
- Eligible blocks (age class >= 40): 393755
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.60 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 17.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
