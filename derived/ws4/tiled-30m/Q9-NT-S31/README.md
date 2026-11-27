# WS4 tiled 30-m dataset — Q9|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q9|NT|S31` (parent `Q9|NT`)
- Tile / row / col: `Q9` / 3 / 1
- Province: `NT`
- Centroid: 66.252662, -121.836995
- Allocated harvest: 45.367961 m3
- Productive subcell area: 76940.164223 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 677450
- Blocks: 329051
- Forest area: 60970.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28133
- Scheduled area: 4891.50 ha
- Eligible blocks (age class >= 40): 281330
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.86 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 10.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
