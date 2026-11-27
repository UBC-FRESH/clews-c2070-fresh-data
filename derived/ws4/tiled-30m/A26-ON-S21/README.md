# WS4 tiled 30-m dataset — A26|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A26|ON|S21` (parent `A26|ON`)
- Tile / row / col: `A26` / 2 / 1
- Province: `ON`
- Centroid: 44.346473, -77.407748
- Allocated harvest: 32874.483640 m3
- Productive subcell area: 130913.520723 ha
- Committed geometry area: 241584.498472 ha
- Clipped inventory geometry: 241584.498472 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1457723
- Blocks: 608787
- Forest area: 131195.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50105
- Scheduled area: 11533.32 ha
- Eligible blocks (age class >= 40): 501042
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.24 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 19.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
