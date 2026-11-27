# WS4 tiled 30-m dataset — D17|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D17|ON|S32` (parent `D17|ON`)
- Tile / row / col: `D17` / 3 / 2
- Province: `ON`
- Centroid: 50.552700, -93.380721
- Allocated harvest: 44486.455537 m3
- Productive subcell area: 192442.146404 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2114805
- Blocks: 772772
- Forest area: 190332.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 71281
- Scheduled area: 16273.08 ha
- Eligible blocks (age class >= 40): 712803
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.80 MB
- Schedules: 0.85 MB
- Runs: 0.00 MB
- Total: 26.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
