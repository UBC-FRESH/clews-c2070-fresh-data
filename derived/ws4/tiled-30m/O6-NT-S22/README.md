# WS4 tiled 30-m dataset — O6|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O6|NT|S22` (parent `O6|NT`)
- Tile / row / col: `O6` / 2 / 2
- Province: `NT`
- Centroid: 61.713903, -126.157922
- Allocated harvest: 101.797925 m3
- Productive subcell area: 122838.100117 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1761248
- Blocks: 781368
- Forest area: 158512.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 67955
- Scheduled area: 13279.95 ha
- Eligible blocks (age class >= 40): 679541
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.43 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 24.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
