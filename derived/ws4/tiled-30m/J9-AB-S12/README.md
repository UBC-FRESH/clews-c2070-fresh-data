# WS4 tiled 30-m dataset — J9|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J9|AB|S12` (parent `J9|AB`)
- Tile / row / col: `J9` / 1 / 2
- Province: `AB`
- Centroid: 56.430546, -113.248735
- Allocated harvest: 105766.628084 m3
- Productive subcell area: 224033.462209 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2635697
- Blocks: 880156
- Forest area: 237212.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 85681
- Scheduled area: 22413.33 ha
- Eligible blocks (age class >= 40): 856808
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.61 MB
- Schedules: 1.02 MB
- Runs: 0.00 MB
- Total: 32.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
