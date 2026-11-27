# WS4 tiled 30-m dataset — F14|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F14|MB|S23` (parent `F14|MB`)
- Tile / row / col: `F14` / 2 / 3
- Province: `MB`
- Centroid: 52.746565, -99.292149
- Allocated harvest: 5981.286535 m3
- Productive subcell area: 126848.865485 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2011324
- Blocks: 666109
- Forest area: 181019.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63038
- Scheduled area: 17049.87 ha
- Eligible blocks (age class >= 40): 630378
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.81 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 24.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
