# WS4 tiled 30-m dataset — R5|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R5|NT|S13` (parent `R5|NT`)
- Tile / row / col: `R5` / 1 / 3
- Province: `NT`
- Centroid: 64.530224, -131.745660
- Allocated harvest: 4.501988 m3
- Productive subcell area: 6775.174275 ha
- Committed geometry area: 42460.064461 ha
- Clipped inventory geometry: 42460.064461 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 10142
- Blocks: 6975
- Forest area: 912.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 565
- Scheduled area: 61.38 ha
- Eligible blocks (age class >= 40): 565
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.27 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
