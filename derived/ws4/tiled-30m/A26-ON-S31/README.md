# WS4 tiled 30-m dataset — A26|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A26|ON|S31` (parent `A26|ON`)
- Tile / row / col: `A26` / 3 / 1
- Province: `ON`
- Centroid: 44.763885, -77.234435
- Allocated harvest: 34019.653421 m3
- Productive subcell area: 135473.842021 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2235476
- Blocks: 754370
- Forest area: 201192.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69156
- Scheduled area: 18863.91 ha
- Eligible blocks (age class >= 40): 691553
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.87 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 27.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
