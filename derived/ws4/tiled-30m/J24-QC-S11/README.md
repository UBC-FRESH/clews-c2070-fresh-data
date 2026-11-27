# WS4 tiled 30-m dataset — J24|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J24|QC|S11` (parent `J24|QC`)
- Tile / row / col: `J24` / 1 / 1
- Province: `QC`
- Centroid: 56.353160, -76.231478
- Allocated harvest: 8812.987430 m3
- Productive subcell area: 53068.522678 ha
- Committed geometry area: 205726.408450 ha
- Clipped inventory geometry: 205726.408450 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 491202
- Blocks: 199519
- Forest area: 44208.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13354
- Scheduled area: 3107.25 ha
- Eligible blocks (age class >= 40): 133534
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.80 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 6.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
