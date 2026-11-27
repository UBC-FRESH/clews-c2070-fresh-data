# WS4 tiled 30-m dataset — J3|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J3|BC|S33` (parent `J3|BC`)
- Tile / row / col: `J3` / 3 / 3
- Province: `BC`
- Centroid: 54.295581, -126.526871
- Allocated harvest: 79991.178586 m3
- Productive subcell area: 186860.574082 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2587999
- Blocks: 892301
- Forest area: 232919.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79945
- Scheduled area: 16688.88 ha
- Eligible blocks (age class >= 40): 799442
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.82 MB
- Schedules: 0.95 MB
- Runs: 0.00 MB
- Total: 31.77 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
