# WS4 tiled 30-m dataset — I13|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I13|MB|S13` (parent `I13|MB`)
- Tile / row / col: `I13` / 1 / 3
- Province: `MB`
- Centroid: 56.269361, -101.900039
- Allocated harvest: 1472.867826 m3
- Productive subcell area: 47314.611054 ha
- Committed geometry area: 63625.496380 ha
- Clipped inventory geometry: 63625.496380 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 278010
- Blocks: 55281
- Forest area: 25020.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3983
- Scheduled area: 1084.05 ha
- Eligible blocks (age class >= 40): 39826
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.02 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 3.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
