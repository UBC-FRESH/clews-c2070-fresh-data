# WS4 tiled 30-m dataset — I4|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I4|BC|S31` (parent `I4|BC`)
- Tile / row / col: `I4` / 3 / 1
- Province: `BC`
- Centroid: 53.293594, -124.771838
- Allocated harvest: 121739.863305 m3
- Productive subcell area: 226249.614180 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2556599
- Blocks: 743320
- Forest area: 230093.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68635
- Scheduled area: 13673.52 ha
- Eligible blocks (age class >= 40): 686347
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.01 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 28.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
