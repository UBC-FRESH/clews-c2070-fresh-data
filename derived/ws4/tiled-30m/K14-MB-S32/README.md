# WS4 tiled 30-m dataset — K14|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K14|MB|S32` (parent `K14|MB`)
- Tile / row / col: `K14` / 3 / 2
- Province: `MB`
- Centroid: 59.898757, -101.200448
- Allocated harvest: 931.536955 m3
- Productive subcell area: 56056.529390 ha
- Committed geometry area: 110634.208180 ha
- Clipped inventory geometry: 110634.208180 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 538936
- Blocks: 173906
- Forest area: 48504.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12874
- Scheduled area: 4976.64 ha
- Eligible blocks (age class >= 40): 128733
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.80 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 6.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
