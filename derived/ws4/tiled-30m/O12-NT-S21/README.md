# WS4 tiled 30-m dataset — O12|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O12|NT|S21` (parent `O12|NT`)
- Tile / row / col: `O12` / 2 / 1
- Province: `NT`
- Centroid: 64.520430, -109.868979
- Allocated harvest: 2.320764 m3
- Productive subcell area: 4975.140795 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 66604
- Blocks: 55721
- Forest area: 5994.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1878
- Scheduled area: 182.16 ha
- Eligible blocks (age class >= 40): 18772
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.62 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
