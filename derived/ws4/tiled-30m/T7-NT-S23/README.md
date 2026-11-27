# WS4 tiled 30-m dataset — T7|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T7|NT|S23` (parent `T7|NT`)
- Tile / row / col: `T7` / 2 / 3
- Province: `NT`
- Centroid: 68.644661, -130.623242
- Allocated harvest: 143.457501 m3
- Productive subcell area: 147355.144971 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1766162
- Blocks: 857839
- Forest area: 158954.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 67183
- Scheduled area: 11022.66 ha
- Eligible blocks (age class >= 40): 671823
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.41 MB
- Schedules: 0.80 MB
- Runs: 0.00 MB
- Total: 25.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
