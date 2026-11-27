# WS4 tiled 30-m dataset — C22|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C22|ON|S33` (parent `C22|ON`)
- Tile / row / col: `C22` / 3 / 3
- Province: `ON`
- Centroid: 48.409764, -82.603216
- Allocated harvest: 61578.724163 m3
- Productive subcell area: 223056.778909 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2543538
- Blocks: 963224
- Forest area: 228918.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 86050
- Scheduled area: 18342.63 ha
- Eligible blocks (age class >= 40): 860495
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.78 MB
- Schedules: 1.02 MB
- Runs: 0.00 MB
- Total: 32.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
