# WS4 tiled 30-m dataset — K2|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K2|BC|S33` (parent `K2|BC`)
- Tile / row / col: `K2` / 3 / 3
- Province: `BC`
- Centroid: 54.794953, -129.725736
- Allocated harvest: 115915.337810 m3
- Productive subcell area: 162566.802983 ha
- Committed geometry area: 231045.152400 ha
- Clipped inventory geometry: 231045.152400 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1607572
- Blocks: 908269
- Forest area: 144681.48 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 87273
- Scheduled area: 13602.33 ha
- Eligible blocks (age class >= 40): 872724
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.63 MB
- Schedules: 1.04 MB
- Runs: 0.00 MB
- Total: 24.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
