# WS4 tiled 30-m dataset — O10|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O10|NT|S22` (parent `O10|NT`)
- Tile / row / col: `O10` / 2 / 2
- Province: `NT`
- Centroid: 63.894102, -114.981869
- Allocated harvest: 51.633304 m3
- Productive subcell area: 87530.451398 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1368301
- Blocks: 426537
- Forest area: 123147.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21754
- Scheduled area: 7633.53 ha
- Eligible blocks (age class >= 40): 217540
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.22 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 15.47 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
