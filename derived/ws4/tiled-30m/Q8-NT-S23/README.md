# WS4 tiled 30-m dataset — Q8|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q8|NT|S23` (parent `Q8|NT`)
- Tile / row / col: `Q8` / 2 / 3
- Province: `NT`
- Centroid: 65.640520, -122.400038
- Allocated harvest: 85.018287 m3
- Productive subcell area: 138418.897170 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 882425
- Blocks: 365032
- Forest area: 79418.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31412
- Scheduled area: 6316.02 ha
- Eligible blocks (age class >= 40): 314119
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.67 MB
- Schedules: 0.37 MB
- Runs: 0.00 MB
- Total: 12.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
