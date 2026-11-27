# WS4 tiled 30-m dataset — J31|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J31|NL|S13` (parent `J31|NL`)
- Tile / row / col: `J31` / 1 / 3
- Province: `NL`
- Centroid: 52.112591, -59.904310
- Allocated harvest: 7900.204257 m3
- Productive subcell area: 110207.329601 ha
- Committed geometry area: 132553.766778 ha
- Clipped inventory geometry: 132553.766778 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1307925
- Blocks: 369717
- Forest area: 117713.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35504
- Scheduled area: 11307.60 ha
- Eligible blocks (age class >= 40): 355033
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.11 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 15.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
