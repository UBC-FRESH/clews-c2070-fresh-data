# WS4 tiled 30-m dataset — M11|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M11|NT|S12` (parent `M11|NT`)
- Tile / row / col: `M11` / 1 / 2
- Province: `NT`
- Centroid: 61.156147, -110.179000
- Allocated harvest: 117.560313 m3
- Productive subcell area: 145246.854703 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1348399
- Blocks: 332940
- Forest area: 121355.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13163
- Scheduled area: 2279.97 ha
- Eligible blocks (age class >= 40): 131622
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.86 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 14.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
