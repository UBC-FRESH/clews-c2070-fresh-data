# WS4 tiled 30-m dataset — H13|SK|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H13|SK|S23` (parent `H13|SK`)
- Tile / row / col: `H13` / 2 / 3
- Province: `SK`
- Centroid: 55.348108, -102.180587
- Allocated harvest: 20180.700249 m3
- Productive subcell area: 110510.697674 ha
- Committed geometry area: 153150.318381 ha
- Clipped inventory geometry: 153150.318381 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1293651
- Blocks: 324405
- Forest area: 116428.59 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22413
- Scheduled area: 4215.42 ha
- Eligible blocks (age class >= 40): 224126
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.67 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 13.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
