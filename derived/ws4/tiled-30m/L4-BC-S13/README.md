# WS4 tiled 30-m dataset — L4|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L4|BC|S13` (parent `L4|BC`)
- Tile / row / col: `L4` / 1 / 3
- Province: `BC`
- Centroid: 56.560091, -125.914197
- Allocated harvest: 55114.838801 m3
- Productive subcell area: 155049.257483 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1590014
- Blocks: 736461
- Forest area: 143101.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66325
- Scheduled area: 12089.43 ha
- Eligible blocks (age class >= 40): 663250
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.75 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 22.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
