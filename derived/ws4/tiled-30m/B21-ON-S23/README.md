# WS4 tiled 30-m dataset — B21|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B21|ON|S23` (parent `B21|ON`)
- Tile / row / col: `B21` / 2 / 3
- Province: `ON`
- Centroid: 47.012945, -84.719281
- Allocated harvest: 3860.566123 m3
- Productive subcell area: 10211.271066 ha
- Committed geometry area: 11137.487140 ha
- Clipped inventory geometry: 11137.487140 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 118046
- Blocks: 21279
- Forest area: 10624.14 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2020
- Scheduled area: 780.21 ha
- Eligible blocks (age class >= 40): 20192
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.42 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
