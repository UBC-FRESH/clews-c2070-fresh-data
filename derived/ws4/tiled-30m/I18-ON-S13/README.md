# WS4 tiled 30-m dataset — I18|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I18|ON|S13` (parent `I18|ON`)
- Tile / row / col: `I18` / 1 / 3
- Province: `ON`
- Centroid: 56.304836, -89.627833
- Allocated harvest: 2811.188225 m3
- Productive subcell area: 54805.732969 ha
- Committed geometry area: 116244.293016 ha
- Clipped inventory geometry: 116244.293016 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 668729
- Blocks: 233999
- Forest area: 60185.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16146
- Scheduled area: 4496.67 ha
- Eligible blocks (age class >= 40): 161456
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.43 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 8.62 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
