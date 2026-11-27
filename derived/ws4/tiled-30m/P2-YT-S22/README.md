# WS4 tiled 30-m dataset — P2|YT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P2|YT|S22` (parent `P2|YT`)
- Tile / row / col: `P2` / 2 / 2
- Province: `YT`
- Centroid: 60.056541, -137.199184
- Allocated harvest: 22.417093 m3
- Productive subcell area: 9746.177935 ha
- Committed geometry area: 34348.304480 ha
- Clipped inventory geometry: 34348.304480 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 178922
- Blocks: 107349
- Forest area: 16102.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9705
- Scheduled area: 1375.56 ha
- Eligible blocks (age class >= 40): 97050
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.55 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 3.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
