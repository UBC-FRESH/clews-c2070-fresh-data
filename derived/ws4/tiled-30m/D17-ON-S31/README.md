# WS4 tiled 30-m dataset — D17|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D17|ON|S31` (parent `D17|ON`)
- Tile / row / col: `D17` / 3 / 1
- Province: `ON`
- Centroid: 50.561687, -94.090240
- Allocated harvest: 44486.455537 m3
- Productive subcell area: 192442.146404 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2270296
- Blocks: 871544
- Forest area: 204326.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77205
- Scheduled area: 15461.01 ha
- Eligible blocks (age class >= 40): 772045
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.30 MB
- Schedules: 0.92 MB
- Runs: 0.00 MB
- Total: 29.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
