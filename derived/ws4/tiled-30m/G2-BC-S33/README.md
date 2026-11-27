# WS4 tiled 30-m dataset — G2|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G2|BC|S33` (parent `G2|BC`)
- Tile / row / col: `G2` / 3 / 3
- Province: `BC`
- Centroid: 50.039515, -125.442447
- Allocated harvest: 180138.093537 m3
- Productive subcell area: 177243.543020 ha
- Committed geometry area: 195062.987906 ha
- Clipped inventory geometry: 195062.987906 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1913025
- Blocks: 621853
- Forest area: 172172.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55194
- Scheduled area: 11940.39 ha
- Eligible blocks (age class >= 40): 551934
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.16 MB
- Schedules: 0.65 MB
- Runs: 0.00 MB
- Total: 22.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
