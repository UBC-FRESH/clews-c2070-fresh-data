# WS4 tiled 30-m dataset — K1|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K1|BC|S32` (parent `K1|BC`)
- Tile / row / col: `K1` / 3 / 2
- Province: `BC`
- Centroid: 53.826989, -132.395466
- Allocated harvest: 188036.459455 m3
- Productive subcell area: 200287.117643 ha
- Committed geometry area: 213908.182007 ha
- Clipped inventory geometry: 213908.182007 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2111482
- Blocks: 849604
- Forest area: 190033.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 83514
- Scheduled area: 15930.63 ha
- Eligible blocks (age class >= 40): 835140
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.11 MB
- Schedules: 0.99 MB
- Runs: 0.00 MB
- Total: 27.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
