# WS4 tiled 30-m dataset — L1|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L1|BC|S11` (parent `L1|BC`)
- Tile / row / col: `L1` / 1 / 1
- Province: `BC`
- Centroid: 53.909744, -133.058502
- Allocated harvest: 12890.849966 m3
- Productive subcell area: 16769.916906 ha
- Committed geometry area: 17818.080245 ha
- Clipped inventory geometry: 17818.080245 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 193938
- Blocks: 92012
- Forest area: 17454.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9142
- Scheduled area: 1718.46 ha
- Eligible blocks (age class >= 40): 91417
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.31 MB
- Schedules: 0.10 MB
- Runs: 0.00 MB
- Total: 3.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
