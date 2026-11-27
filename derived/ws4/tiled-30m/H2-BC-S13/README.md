# WS4 tiled 30-m dataset — H2|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H2|BC|S13` (parent `H2|BC`)
- Tile / row / col: `H2` / 1 / 3
- Province: `BC`
- Centroid: 50.444319, -125.703901
- Allocated harvest: 151175.387503 m3
- Productive subcell area: 172299.339219 ha
- Committed geometry area: 207616.489932 ha
- Clipped inventory geometry: 207616.489932 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2173617
- Blocks: 739161
- Forest area: 195625.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69893
- Scheduled area: 13607.64 ha
- Eligible blocks (age class >= 40): 698928
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.10 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 25.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
