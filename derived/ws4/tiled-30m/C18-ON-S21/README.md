# WS4 tiled 30-m dataset — C18|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C18|ON|S21` (parent `C18|ON`)
- Tile / row / col: `C18` / 2 / 1
- Province: `ON`
- Centroid: 48.719186, -92.092652
- Allocated harvest: 42978.519913 m3
- Productive subcell area: 198681.129932 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2267952
- Blocks: 847095
- Forest area: 204115.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73235
- Scheduled area: 15235.74 ha
- Eligible blocks (age class >= 40): 732341
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.10 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 28.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
