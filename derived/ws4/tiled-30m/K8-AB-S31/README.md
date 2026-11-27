# WS4 tiled 30-m dataset — K8|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K8|AB|S31` (parent `K8|AB`)
- Tile / row / col: `K8` / 3 / 1
- Province: `AB`
- Centroid: 58.028769, -117.811285
- Allocated harvest: 121093.191000 m3
- Productive subcell area: 204039.481003 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2144624
- Blocks: 995866
- Forest area: 193016.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 87992
- Scheduled area: 15027.66 ha
- Eligible blocks (age class >= 40): 879915
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.82 MB
- Schedules: 1.05 MB
- Runs: 0.00 MB
- Total: 29.87 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
