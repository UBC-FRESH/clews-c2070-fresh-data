# WS4 tiled 30-m dataset — G2|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G2|BC|S21` (parent `G2|BC`)
- Tile / row / col: `G2` / 2 / 1
- Province: `BC`
- Centroid: 49.353558, -126.138912
- Allocated harvest: 49502.324788 m3
- Productive subcell area: 48706.896253 ha
- Committed geometry area: 53603.716970 ha
- Clipped inventory geometry: 53603.716970 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 577718
- Blocks: 297870
- Forest area: 51994.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29602
- Scheduled area: 4779.81 ha
- Eligible blocks (age class >= 40): 296015
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.64 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 8.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
