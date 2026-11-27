# WS4 tiled 30-m dataset — D24|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D24|QC|S21` (parent `D24|QC`)
- Tile / row / col: `D24` / 2 / 1
- Province: `QC`
- Centroid: 48.892521, -79.419052
- Allocated harvest: 22840.344672 m3
- Productive subcell area: 57576.463637 ha
- Committed geometry area: 70125.355193 ha
- Clipped inventory geometry: 70125.355193 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 493784
- Blocks: 212653
- Forest area: 44440.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16904
- Scheduled area: 3221.55 ha
- Eligible blocks (age class >= 40): 169038
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.14 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 7.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
