# WS4 tiled 30-m dataset — F4|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F4|BC|S11` (parent `F4|BC`)
- Tile / row / col: `F4` / 1 / 1
- Province: `BC`
- Centroid: 49.028821, -121.300506
- Allocated harvest: 9277.832735 m3
- Productive subcell area: 9227.499758 ha
- Committed geometry area: 12342.005325 ha
- Clipped inventory geometry: 12342.005325 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 112195
- Blocks: 58492
- Forest area: 10097.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5618
- Scheduled area: 1014.75 ha
- Eligible blocks (age class >= 40): 56174
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.09 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 2.15 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
