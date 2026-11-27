# WS4 tiled 30-m dataset — L11|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L11|AB|S12` (parent `L11|AB`)
- Tile / row / col: `L11` / 1 / 2
- Province: `AB`
- Centroid: 59.925677, -110.027398
- Allocated harvest: 711.994633 m3
- Productive subcell area: 3371.784763 ha
- Committed geometry area: 4365.832713 ha
- Clipped inventory geometry: 4365.832713 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 39438
- Blocks: 3594
- Forest area: 3549.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3498
- Scheduled area: 3537.99 ha
- Eligible blocks (age class >= 40): 3498
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.41 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
