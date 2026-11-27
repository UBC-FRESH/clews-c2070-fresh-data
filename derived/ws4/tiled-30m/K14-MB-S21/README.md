# WS4 tiled 30-m dataset — K14|MB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K14|MB|S21` (parent `K14|MB`)
- Tile / row / col: `K14` / 2 / 1
- Province: `MB`
- Centroid: 59.524382, -101.788815
- Allocated harvest: 1013.766689 m3
- Productive subcell area: 61004.817767 ha
- Committed geometry area: 120400.242080 ha
- Clipped inventory geometry: 120400.242080 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 783763
- Blocks: 241603
- Forest area: 70538.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19364
- Scheduled area: 4185.18 ha
- Eligible blocks (age class >= 40): 193632
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.08 MB
- Schedules: 0.22 MB
- Runs: 0.00 MB
- Total: 9.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
