# WS4 tiled 30-m dataset — L12|SK|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L12|SK|S11` (parent `L12|SK`)
- Tile / row / col: `L12` / 1 / 1
- Province: `SK`
- Centroid: 59.887714, -107.718012
- Allocated harvest: 5822.382233 m3
- Productive subcell area: 77066.776750 ha
- Committed geometry area: 122833.845115 ha
- Clipped inventory geometry: 122833.845115 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 965147
- Blocks: 189426
- Forest area: 86863.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10331
- Scheduled area: 6413.04 ha
- Eligible blocks (age class >= 40): 103307
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.32 MB
- Schedules: 0.12 MB
- Runs: 0.00 MB
- Total: 9.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
