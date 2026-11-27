# WS4 tiled 30-m dataset — F14|MB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F14|MB|S21` (parent `F14|MB`)
- Tile / row / col: `F14` / 2 / 1
- Province: `MB`
- Centroid: 52.674525, -100.786166
- Allocated harvest: 5981.286535 m3
- Productive subcell area: 126848.865485 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1671674
- Blocks: 539897
- Forest area: 150450.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50276
- Scheduled area: 13081.14 ha
- Eligible blocks (age class >= 40): 502752
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.87 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 20.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
