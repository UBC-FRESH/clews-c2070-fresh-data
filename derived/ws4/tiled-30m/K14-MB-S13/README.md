# WS4 tiled 30-m dataset — K14|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K14|MB|S13` (parent `K14|MB`)
- Tile / row / col: `K14` / 1 / 3
- Province: `MB`
- Centroid: 59.149018, -100.139761
- Allocated harvest: 2104.993045 m3
- Productive subcell area: 126670.878548 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1443071
- Blocks: 360153
- Forest area: 129876.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23789
- Scheduled area: 7781.31 ha
- Eligible blocks (age class >= 40): 237887
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.00 MB
- Schedules: 0.28 MB
- Runs: 0.00 MB
- Total: 15.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
