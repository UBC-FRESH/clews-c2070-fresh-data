# WS4 tiled 30-m dataset — C28|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C28|QC|S32` (parent `C28|QC`)
- Tile / row / col: `C28` / 3 / 2
- Province: `QC`
- Centroid: 46.306382, -71.846978
- Allocated harvest: 73450.257310 m3
- Productive subcell area: 133166.740271 ha
- Committed geometry area: 248899.242720 ha
- Clipped inventory geometry: 248899.242720 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1842799
- Blocks: 582454
- Forest area: 165851.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49140
- Scheduled area: 14387.22 ha
- Eligible blocks (age class >= 40): 491395
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.66 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 22.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
