# WS4 tiled 30-m dataset — Q9|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q9|NT|S23` (parent `Q9|NT`)
- Tile / row / col: `Q9` / 2 / 3
- Province: `NT`
- Centroid: 66.188799, -119.281116
- Allocated harvest: 45.367961 m3
- Productive subcell area: 76940.164223 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 128654
- Blocks: 56942
- Forest area: 11578.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3143
- Scheduled area: 676.44 ha
- Eligible blocks (age class >= 40): 31427
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.19 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 2.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
