# WS4 tiled 30-m dataset — C28|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C28|QC|S13` (parent `C28|QC`)
- Tile / row / col: `C28` / 1 / 3
- Province: `QC`
- Centroid: 45.320006, -71.708252
- Allocated harvest: 73737.162749 m3
- Productive subcell area: 133686.905393 ha
- Committed geometry area: 249871.472758 ha
- Clipped inventory geometry: 249871.472758 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1955165
- Blocks: 604119
- Forest area: 175964.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49401
- Scheduled area: 15035.22 ha
- Eligible blocks (age class >= 40): 494002
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.59 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 23.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
