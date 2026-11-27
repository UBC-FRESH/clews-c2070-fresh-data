# WS4 tiled 30-m dataset — A26|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A26|ON|S32` (parent `A26|ON`)
- Tile / row / col: `A26` / 3 / 2
- Province: `ON`
- Centroid: 44.640159, -76.640050
- Allocated harvest: 34019.653421 m3
- Productive subcell area: 135473.842021 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1927950
- Blocks: 682322
- Forest area: 173515.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59806
- Scheduled area: 15899.31 ha
- Eligible blocks (age class >= 40): 598060
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.38 MB
- Schedules: 0.71 MB
- Runs: 0.00 MB
- Total: 24.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
