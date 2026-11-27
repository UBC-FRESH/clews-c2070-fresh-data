# WS4 tiled 30-m dataset — L4|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L4|BC|S11` (parent `L4|BC`)
- Tile / row / col: `L4` / 1 / 1
- Province: `BC`
- Centroid: 56.121886, -127.367188
- Allocated harvest: 55114.838801 m3
- Productive subcell area: 155049.257483 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1806418
- Blocks: 898501
- Forest area: 162577.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 85381
- Scheduled area: 15202.35 ha
- Eligible blocks (age class >= 40): 853807
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.22 MB
- Schedules: 1.01 MB
- Runs: 0.00 MB
- Total: 26.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
