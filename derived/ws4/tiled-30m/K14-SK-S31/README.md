# WS4 tiled 30-m dataset — K14|SK|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K14|SK|S31` (parent `K14|SK`)
- Tile / row / col: `K14` / 3 / 1
- Province: `SK`
- Centroid: 59.871755, -102.288386
- Allocated harvest: 3911.612907 m3
- Productive subcell area: 50015.317302 ha
- Committed geometry area: 86321.759759 ha
- Clipped inventory geometry: 86321.759759 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 584021
- Blocks: 141179
- Forest area: 52561.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11905
- Scheduled area: 4092.48 ha
- Eligible blocks (age class >= 40): 119048
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.58 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 6.72 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
