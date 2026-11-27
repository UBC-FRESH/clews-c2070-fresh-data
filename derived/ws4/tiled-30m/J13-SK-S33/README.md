# WS4 tiled 30-m dataset — J13|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J13|SK|S33` (parent `J13|SK`)
- Tile / row / col: `J13` / 3 / 3
- Province: `SK`
- Centroid: 58.550749, -102.705794
- Allocated harvest: 12328.514886 m3
- Productive subcell area: 149350.626558 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1701311
- Blocks: 305172
- Forest area: 153117.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25040
- Scheduled area: 7580.79 ha
- Eligible blocks (age class >= 40): 250395
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.67 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 15.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
