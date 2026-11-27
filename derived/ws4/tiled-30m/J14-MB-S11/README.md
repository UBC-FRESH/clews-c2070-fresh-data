# WS4 tiled 30-m dataset — J14|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J14|MB|S11` (parent `J14|MB`)
- Tile / row / col: `J14` / 1 / 1
- Province: `MB`
- Centroid: 57.684562, -101.611212
- Allocated harvest: 2492.271793 m3
- Productive subcell area: 138082.442923 ha
- Committed geometry area: 230510.389533 ha
- Clipped inventory geometry: 230510.389533 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1307094
- Blocks: 336557
- Forest area: 117638.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29153
- Scheduled area: 9109.71 ha
- Eligible blocks (age class >= 40): 291522
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.12 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 14.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
