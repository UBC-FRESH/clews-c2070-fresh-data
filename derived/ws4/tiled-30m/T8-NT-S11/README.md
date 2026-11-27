# WS4 tiled 30-m dataset — T8|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T8|NT|S11` (parent `T8|NT`)
- Tile / row / col: `T8` / 1 / 1
- Province: `NT`
- Centroid: 68.490338, -128.891247
- Allocated harvest: 5.324897 m3
- Productive subcell area: 11779.760064 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1957736
- Blocks: 794307
- Forest area: 176196.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69098
- Scheduled area: 15721.38 ha
- Eligible blocks (age class >= 40): 690974
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.84 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 25.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
