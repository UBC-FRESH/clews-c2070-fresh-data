# WS4 tiled 30-m dataset — C24|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C24|QC|S22` (parent `C24|QC`)
- Tile / row / col: `C24` / 2 / 2
- Province: `QC`
- Centroid: 47.480743, -79.349420
- Allocated harvest: 59973.909070 m3
- Productive subcell area: 107612.156449 ha
- Committed geometry area: 136865.713865 ha
- Clipped inventory geometry: 136865.713865 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 881256
- Blocks: 336876
- Forest area: 79313.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29322
- Scheduled area: 6671.25 ha
- Eligible blocks (age class >= 40): 293219
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.49 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 11.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
