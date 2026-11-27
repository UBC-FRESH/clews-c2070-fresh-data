# WS4 tiled 30-m dataset — D31|NB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D31|NB|S33` (parent `D31|NB`)
- Tile / row / col: `D31` / 3 / 3
- Province: `NB`
- Centroid: 45.740220, -65.243711
- Allocated harvest: 188847.045554 m3
- Productive subcell area: 210537.725095 ha
- Committed geometry area: 240783.651983 ha
- Clipped inventory geometry: 240783.651983 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2315913
- Blocks: 855365
- Forest area: 208432.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69466
- Scheduled area: 14252.04 ha
- Eligible blocks (age class >= 40): 694657
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.40 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 29.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
