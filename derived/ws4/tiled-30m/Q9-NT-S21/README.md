# WS4 tiled 30-m dataset — Q9|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q9|NT|S21` (parent `Q9|NT`)
- Tile / row / col: `Q9` / 2 / 1
- Province: `NT`
- Centroid: 65.830219, -121.375064
- Allocated harvest: 45.367961 m3
- Productive subcell area: 76940.164223 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 286757
- Blocks: 134452
- Forest area: 25808.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11831
- Scheduled area: 2233.08 ha
- Eligible blocks (age class >= 40): 118306
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.78 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 4.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
