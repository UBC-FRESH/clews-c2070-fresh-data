# WS4 tiled 30-m dataset — G12|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G12|SK|S33` (parent `G12|SK`)
- Tile / row / col: `G12` / 3 / 3
- Province: `SK`
- Centroid: 54.272552, -104.181993
- Allocated harvest: 32142.591788 m3
- Productive subcell area: 162615.589192 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1854699
- Blocks: 639340
- Forest area: 166922.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59961
- Scheduled area: 13088.88 ha
- Eligible blocks (age class >= 40): 599602
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.11 MB
- Schedules: 0.71 MB
- Runs: 0.00 MB
- Total: 22.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
