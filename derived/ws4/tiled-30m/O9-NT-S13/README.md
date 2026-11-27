# WS4 tiled 30-m dataset — O9|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O9|NT|S13` (parent `O9|NT`)
- Tile / row / col: `O9` / 1 / 3
- Province: `NT`
- Centroid: 63.158731, -116.612100
- Allocated harvest: 90.559773 m3
- Productive subcell area: 115433.428079 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1511130
- Blocks: 706414
- Forest area: 136001.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53220
- Scheduled area: 9385.11 ha
- Eligible blocks (age class >= 40): 532197
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.63 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 21.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
