# WS4 tiled 30-m dataset — G31|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G31|QC|S11` (parent `G31|QC`)
- Tile / row / col: `G31` / 1 / 1
- Province: `QC`
- Centroid: 48.869299, -64.472542
- Allocated harvest: 36622.866115 m3
- Productive subcell area: 81568.006034 ha
- Committed geometry area: 95738.663515 ha
- Clipped inventory geometry: 95738.663515 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 974218
- Blocks: 383841
- Forest area: 87679.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36054
- Scheduled area: 8363.61 ha
- Eligible blocks (age class >= 40): 360538
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.65 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 13.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
