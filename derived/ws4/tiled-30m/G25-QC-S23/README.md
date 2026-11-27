# WS4 tiled 30-m dataset — G25|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G25|QC|S23` (parent `G25|QC`)
- Tile / row / col: `G25` / 2 / 3
- Province: `QC`
- Centroid: 52.179772, -74.479799
- Allocated harvest: 36100.529959 m3
- Productive subcell area: 145164.027264 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1560493
- Blocks: 617238
- Forest area: 140444.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45463
- Scheduled area: 8897.22 ha
- Eligible blocks (age class >= 40): 454628
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.74 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 20.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
