# WS4 tiled 30-m dataset — C15|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C15|MB|S31` (parent `C15|MB`)
- Tile / row / col: `C15` / 3 / 1
- Province: `MB`
- Centroid: 49.192135, -98.237117
- Allocated harvest: 1451.577769 m3
- Productive subcell area: 34473.625119 ha
- Committed geometry area: 212843.874962 ha
- Clipped inventory geometry: 212843.874962 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 321101
- Blocks: 81999
- Forest area: 28899.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4071
- Scheduled area: 1903.50 ha
- Eligible blocks (age class >= 40): 40703
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.82 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 3.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
