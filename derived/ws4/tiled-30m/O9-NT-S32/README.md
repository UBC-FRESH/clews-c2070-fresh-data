# WS4 tiled 30-m dataset — O9|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O9|NT|S32` (parent `O9|NT`)
- Tile / row / col: `O9` / 3 / 2
- Province: `NT`
- Centroid: 63.867047, -118.300586
- Allocated harvest: 90.559773 m3
- Productive subcell area: 115433.428079 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1636832
- Blocks: 754225
- Forest area: 147314.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59771
- Scheduled area: 10591.92 ha
- Eligible blocks (age class >= 40): 597708
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.15 MB
- Schedules: 0.71 MB
- Runs: 0.00 MB
- Total: 22.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
