# WS4 tiled 30-m dataset — L13|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L13|NT|S12` (parent `L13|NT`)
- Tile / row / col: `L13` / 1 / 2
- Province: `NT`
- Centroid: 60.319681, -104.080430
- Allocated harvest: 40.712733 m3
- Productive subcell area: 104674.290360 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1735944
- Blocks: 391606
- Forest area: 156234.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33645
- Scheduled area: 8452.98 ha
- Eligible blocks (age class >= 40): 336444
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.91 MB
- Schedules: 0.39 MB
- Runs: 0.00 MB
- Total: 17.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
