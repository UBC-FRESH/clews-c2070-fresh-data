# WS4 tiled 30-m dataset — K4|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K4|BC|S31` (parent `K4|BC`)
- Tile / row / col: `K4` / 3 / 1
- Province: `BC`
- Centroid: 55.720578, -126.971395
- Allocated harvest: 84412.572477 m3
- Productive subcell area: 216445.726840 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2332064
- Blocks: 1137092
- Forest area: 209885.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 108720
- Scheduled area: 18483.66 ha
- Eligible blocks (age class >= 40): 1087199
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 32.68 MB
- Schedules: 1.31 MB
- Runs: 0.00 MB
- Total: 33.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
