# WS4 tiled 30-m dataset — E5|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E5|BC|S32` (parent `E5|BC`)
- Tile / row / col: `E5` / 3 / 2
- Province: `BC`
- Centroid: 49.140902, -118.623511
- Allocated harvest: 113817.350966 m3
- Productive subcell area: 136221.530933 ha
- Committed geometry area: 162420.238659 ha
- Clipped inventory geometry: 162420.238659 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1479933
- Blocks: 705247
- Forest area: 133193.97 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 61712
- Scheduled area: 9544.50 ha
- Eligible blocks (age class >= 40): 617119
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.82 MB
- Schedules: 0.73 MB
- Runs: 0.00 MB
- Total: 21.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
