# WS4 tiled 30-m dataset — L10|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L10|AB|S21` (parent `L10|AB`)
- Tile / row / col: `L10` / 2 / 1
- Province: `AB`
- Centroid: 59.772554, -113.313330
- Allocated harvest: 90073.669831 m3
- Productive subcell area: 192334.218762 ha
- Committed geometry area: 239612.560084 ha
- Clipped inventory geometry: 239612.560084 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2157784
- Blocks: 812671
- Forest area: 194200.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65077
- Scheduled area: 12519.27 ha
- Eligible blocks (age class >= 40): 650761
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.29 MB
- Schedules: 0.77 MB
- Runs: 0.00 MB
- Total: 27.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
