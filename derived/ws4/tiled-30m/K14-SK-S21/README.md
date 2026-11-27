# WS4 tiled 30-m dataset — K14|SK|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K14|SK|S21` (parent `K14|SK`)
- Tile / row / col: `K14` / 2 / 1
- Province: `SK`
- Centroid: 59.515945, -102.241992
- Allocated harvest: 5872.726498 m3
- Productive subcell area: 75090.834949 ha
- Committed geometry area: 129599.757920 ha
- Clipped inventory geometry: 129599.757920 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 844953
- Blocks: 202735
- Forest area: 76045.77 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16312
- Scheduled area: 3978.00 ha
- Eligible blocks (age class >= 40): 163120
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.74 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 8.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
