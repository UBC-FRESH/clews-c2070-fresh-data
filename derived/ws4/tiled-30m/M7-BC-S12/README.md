# WS4 tiled 30-m dataset — M7|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|BC|S12` (parent `M7|BC`)
- Tile / row / col: `M7` / 1 / 2
- Province: `BC`
- Centroid: 59.396515, -120.776869
- Allocated harvest: 72421.782174 m3
- Productive subcell area: 178443.689183 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1842967
- Blocks: 610175
- Forest area: 165867.03 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46497
- Scheduled area: 9598.41 ha
- Eligible blocks (age class >= 40): 464963
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.26 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 21.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
