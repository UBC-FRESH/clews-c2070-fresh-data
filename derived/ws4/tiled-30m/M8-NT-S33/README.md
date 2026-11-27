# WS4 tiled 30-m dataset — M8|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M8|NT|S33` (parent `M8|NT`)
- Tile / row / col: `M8` / 3 / 3
- Province: `NT`
- Centroid: 60.944723, -118.032844
- Allocated harvest: 154.254008 m3
- Productive subcell area: 110912.963160 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1258668
- Blocks: 410139
- Forest area: 113280.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29579
- Scheduled area: 7384.50 ha
- Eligible blocks (age class >= 40): 295785
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.01 MB
- Schedules: 0.35 MB
- Runs: 0.00 MB
- Total: 15.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
