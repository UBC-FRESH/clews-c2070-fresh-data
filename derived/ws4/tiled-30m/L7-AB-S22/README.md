# WS4 tiled 30-m dataset — L7|AB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|AB|S22` (parent `L7|AB`)
- Tile / row / col: `L7` / 2 / 2
- Province: `AB`
- Centroid: 58.559873, -119.822584
- Allocated harvest: 47660.205409 m3
- Productive subcell area: 84411.923506 ha
- Committed geometry area: 99920.699830 ha
- Clipped inventory geometry: 99920.699830 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 888348
- Blocks: 340369
- Forest area: 79951.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25670
- Scheduled area: 4123.62 ha
- Eligible blocks (age class >= 40): 256691
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.22 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 11.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
