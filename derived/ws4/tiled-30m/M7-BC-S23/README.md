# WS4 tiled 30-m dataset — M7|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|BC|S23` (parent `M7|BC`)
- Tile / row / col: `M7` / 2 / 3
- Province: `BC`
- Centroid: 59.881477, -120.364788
- Allocated harvest: 28905.504019 m3
- Productive subcell area: 71221.732191 ha
- Committed geometry area: 99781.803040 ha
- Clipped inventory geometry: 99781.803040 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 632694
- Blocks: 132259
- Forest area: 56942.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8820
- Scheduled area: 1736.01 ha
- Eligible blocks (age class >= 40): 88191
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.40 MB
- Schedules: 0.10 MB
- Runs: 0.00 MB
- Total: 6.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
