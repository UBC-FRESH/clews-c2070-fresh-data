# WS4 tiled 30-m dataset — K1|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K1|BC|S21` (parent `K1|BC`)
- Tile / row / col: `K1` / 2 / 1
- Province: `BC`
- Centroid: 53.234462, -132.418193
- Allocated harvest: 89575.138849 m3
- Productive subcell area: 95410.998615 ha
- Committed geometry area: 101899.680306 ha
- Clipped inventory geometry: 101899.680306 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1072854
- Blocks: 510666
- Forest area: 96556.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50344
- Scheduled area: 9396.90 ha
- Eligible blocks (age class >= 40): 503436
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.62 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 15.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
