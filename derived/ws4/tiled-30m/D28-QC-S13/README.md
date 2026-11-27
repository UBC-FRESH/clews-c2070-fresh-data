# WS4 tiled 30-m dataset — D28|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D28|QC|S13` (parent `D28|QC`)
- Tile / row / col: `D28` / 1 / 3
- Province: `QC`
- Centroid: 46.559105, -71.013087
- Allocated harvest: 115134.570058 m3
- Productive subcell area: 196335.531670 ha
- Committed geometry area: 247838.611985 ha
- Clipped inventory geometry: 247838.611985 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1511812
- Blocks: 544450
- Forest area: 136063.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43355
- Scheduled area: 11196.72 ha
- Eligible blocks (age class >= 40): 433548
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.79 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 19.30 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
