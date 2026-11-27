# WS4 tiled 30-m dataset — K14|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K14|MB|S22` (parent `K14|MB`)
- Tile / row / col: `K14` / 2 / 2
- Province: `MB`
- Centroid: 59.567809, -101.119763
- Allocated harvest: 2104.993045 m3
- Productive subcell area: 126670.878548 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1584260
- Blocks: 381104
- Forest area: 142583.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22663
- Scheduled area: 5531.76 ha
- Eligible blocks (age class >= 40): 226625
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.24 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 16.51 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
