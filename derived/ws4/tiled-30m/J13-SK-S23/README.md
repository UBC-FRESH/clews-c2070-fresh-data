# WS4 tiled 30-m dataset — J13|SK|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J13|SK|S23` (parent `J13|SK`)
- Tile / row / col: `J13` / 2 / 3
- Province: `SK`
- Centroid: 58.093363, -102.600683
- Allocated harvest: 12328.514886 m3
- Productive subcell area: 149350.626558 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1747991
- Blocks: 334865
- Forest area: 157319.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23472
- Scheduled area: 6344.91 ha
- Eligible blocks (age class >= 40): 234717
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.41 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 16.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
