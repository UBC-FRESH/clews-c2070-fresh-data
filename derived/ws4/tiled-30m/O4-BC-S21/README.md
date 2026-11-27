# WS4 tiled 30-m dataset — O4|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O4|BC|S21` (parent `O4|BC`)
- Tile / row / col: `O4` / 2 / 1
- Province: `BC`
- Centroid: 59.915113, -131.855069
- Allocated harvest: 8297.420800 m3
- Productive subcell area: 45891.076131 ha
- Committed geometry area: 84108.735883 ha
- Clipped inventory geometry: 84108.735883 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 866038
- Blocks: 467954
- Forest area: 77943.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45617
- Scheduled area: 7422.93 ha
- Eligible blocks (age class >= 40): 456162
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.82 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 13.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
