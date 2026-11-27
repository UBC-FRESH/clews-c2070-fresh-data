# WS4 tiled 30-m dataset — L13|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L13|NT|S33` (parent `L13|NT`)
- Tile / row / col: `L13` / 3 / 3
- Province: `NT`
- Centroid: 61.298396, -103.402646
- Allocated harvest: 40.712733 m3
- Productive subcell area: 104674.290360 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1019717
- Blocks: 598925
- Forest area: 91774.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43996
- Scheduled area: 6457.41 ha
- Eligible blocks (age class >= 40): 439953
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.53 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 16.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
