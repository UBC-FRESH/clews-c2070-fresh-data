# WS4 tiled 30-m dataset — J28|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J28|QC|S32` (parent `J28|QC`)
- Tile / row / col: `J28` / 3 / 2
- Province: `QC`
- Centroid: 55.057317, -65.827710
- Allocated harvest: 16573.684340 m3
- Productive subcell area: 117516.555613 ha
- Committed geometry area: 193075.301031 ha
- Clipped inventory geometry: 193075.301031 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1381614
- Blocks: 804279
- Forest area: 124345.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74350
- Scheduled area: 11411.46 ha
- Eligible blocks (age class >= 40): 743499
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.82 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 21.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
