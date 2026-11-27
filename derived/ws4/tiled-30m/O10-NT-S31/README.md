# WS4 tiled 30-m dataset — O10|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O10|NT|S31` (parent `O10|NT`)
- Tile / row / col: `O10` / 3 / 1
- Province: `NT`
- Centroid: 64.185019, -116.318964
- Allocated harvest: 51.633304 m3
- Productive subcell area: 87530.451398 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1435418
- Blocks: 530078
- Forest area: 129187.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39848
- Scheduled area: 9541.89 ha
- Eligible blocks (age class >= 40): 398480
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.48 MB
- Schedules: 0.47 MB
- Runs: 0.00 MB
- Total: 17.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
