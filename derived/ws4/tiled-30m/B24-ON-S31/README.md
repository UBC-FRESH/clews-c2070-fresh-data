# WS4 tiled 30-m dataset — B24|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B24|ON|S31` (parent `B24|ON`)
- Tile / row / col: `B24` / 3 / 1
- Province: `ON`
- Centroid: 46.722023, -80.436690
- Allocated harvest: 68244.312992 m3
- Productive subcell area: 257021.272469 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2280168
- Blocks: 860324
- Forest area: 205215.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79059
- Scheduled area: 18113.40 ha
- Eligible blocks (age class >= 40): 790583
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.93 MB
- Schedules: 0.94 MB
- Runs: 0.00 MB
- Total: 29.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
