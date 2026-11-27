# WS4 tiled 30-m dataset — F4|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F4|BC|S12` (parent `F4|BC`)
- Tile / row / col: `F4` / 1 / 2
- Province: `BC`
- Centroid: 49.095498, -120.790869
- Allocated harvest: 79647.840513 m3
- Productive subcell area: 79215.744677 ha
- Committed geometry area: 105952.984912 ha
- Clipped inventory geometry: 105952.984912 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1027746
- Blocks: 504550
- Forest area: 92497.14 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46831
- Scheduled area: 7221.06 ha
- Eligible blocks (age class >= 40): 468310
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.40 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 14.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
