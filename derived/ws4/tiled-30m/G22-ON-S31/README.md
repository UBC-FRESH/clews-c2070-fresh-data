# WS4 tiled 30-m dataset — G22|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G22|ON|S31` (parent `G22|ON`)
- Tile / row / col: `G22` / 3 / 1
- Province: `ON`
- Centroid: 53.904596, -82.444647
- Allocated harvest: 5948.720210 m3
- Productive subcell area: 80380.087862 ha
- Committed geometry area: 168226.119990 ha
- Clipped inventory geometry: 168226.119990 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 779868
- Blocks: 276207
- Forest area: 70188.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22077
- Scheduled area: 5675.31 ha
- Eligible blocks (age class >= 40): 220770
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.91 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 10.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
