# WS4 tiled 30-m dataset — D27|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D27|QC|S22` (parent `D27|QC`)
- Tile / row / col: `D27` / 2 / 2
- Province: `QC`
- Centroid: 47.607321, -73.230842
- Allocated harvest: 120307.451326 m3
- Productive subcell area: 223494.001956 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2451135
- Blocks: 733750
- Forest area: 220602.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 61122
- Scheduled area: 15903.18 ha
- Eligible blocks (age class >= 40): 611218
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.19 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 28.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
