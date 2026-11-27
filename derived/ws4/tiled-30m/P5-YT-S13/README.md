# WS4 tiled 30-m dataset — P5|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P5|YT|S13` (parent `P5|YT`)
- Tile / row / col: `P5` / 1 / 3
- Province: `YT`
- Centroid: 61.986430, -128.907096
- Allocated harvest: 102.816974 m3
- Productive subcell area: 101839.707074 ha
- Committed geometry area: 143965.601880 ha
- Clipped inventory geometry: 143965.601880 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 463300
- Blocks: 209735
- Forest area: 41697.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16463
- Scheduled area: 3388.68 ha
- Eligible blocks (age class >= 40): 164628
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.90 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 7.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
