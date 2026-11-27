# WS4 tiled 30-m dataset — P2|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P2|BC|S22` (parent `P2|BC`)
- Tile / row / col: `P2` / 2 / 2
- Province: `BC`
- Centroid: 59.811184, -137.226324
- Allocated harvest: 8230.696051 m3
- Productive subcell area: 25429.412335 ha
- Committed geometry area: 215651.695520 ha
- Clipped inventory geometry: 215651.695520 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 617985
- Blocks: 327324
- Forest area: 55618.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29432
- Scheduled area: 4896.00 ha
- Eligible blocks (age class >= 40): 294315
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.48 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 9.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
