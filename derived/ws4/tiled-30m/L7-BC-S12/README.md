# WS4 tiled 30-m dataset — L7|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|BC|S12` (parent `L7|BC`)
- Tile / row / col: `L7` / 1 / 2
- Province: `BC`
- Centroid: 58.134547, -120.105373
- Allocated harvest: 16310.878221 m3
- Productive subcell area: 39885.885328 ha
- Committed geometry area: 46567.253268 ha
- Clipped inventory geometry: 46567.253268 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 490506
- Blocks: 179419
- Forest area: 44145.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15958
- Scheduled area: 3514.23 ha
- Eligible blocks (age class >= 40): 159574
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.63 MB
- Schedules: 0.18 MB
- Runs: 0.00 MB
- Total: 6.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
