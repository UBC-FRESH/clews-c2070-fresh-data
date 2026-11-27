# WS4 tiled 30-m dataset — K16|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K16|MB|S31` (parent `K16|MB`)
- Tile / row / col: `K16` / 3 / 1
- Province: `MB`
- Centroid: 59.969185, -96.597239
- Allocated harvest: 105.248323 m3
- Productive subcell area: 5690.885012 ha
- Committed geometry area: 33839.733858 ha
- Clipped inventory geometry: 33839.733858 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 19460
- Blocks: 11856
- Forest area: 1751.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4828
- Scheduled area: 803.88 ha
- Eligible blocks (age class >= 40): 4828
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.45 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 0.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
