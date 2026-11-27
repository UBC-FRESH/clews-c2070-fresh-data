# WS4 tiled 30-m dataset — O6|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O6|YT|S11` (parent `O6|YT`)
- Tile / row / col: `O6` / 1 / 1
- Province: `YT`
- Centroid: 61.150007, -127.054088
- Allocated harvest: 17.201601 m3
- Productive subcell area: 12318.989647 ha
- Committed geometry area: 18282.784538 ha
- Clipped inventory geometry: 18282.784538 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 170321
- Blocks: 62051
- Forest area: 15328.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5511
- Scheduled area: 1400.85 ha
- Eligible blocks (age class >= 40): 55103
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.61 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 2.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
