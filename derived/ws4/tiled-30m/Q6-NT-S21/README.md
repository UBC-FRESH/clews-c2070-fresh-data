# WS4 tiled 30-m dataset — Q6|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q6|NT|S21` (parent `Q6|NT`)
- Tile / row / col: `Q6` / 2 / 1
- Province: `NT`
- Centroid: 63.916713, -129.983644
- Allocated harvest: 21.107422 m3
- Productive subcell area: 34922.716113 ha
- Committed geometry area: 205261.446612 ha
- Clipped inventory geometry: 205261.446612 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 318732
- Blocks: 182590
- Forest area: 28685.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9699
- Scheduled area: 1453.86 ha
- Eligible blocks (age class >= 40): 96984
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.52 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 5.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
