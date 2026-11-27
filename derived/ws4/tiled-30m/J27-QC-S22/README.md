# WS4 tiled 30-m dataset — J27|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J27|QC|S22` (parent `J27|QC`)
- Tile / row / col: `J27` / 2 / 2
- Province: `QC`
- Centroid: 55.185100, -68.390731
- Allocated harvest: 17915.927235 m3
- Productive subcell area: 147541.478934 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1502973
- Blocks: 945399
- Forest area: 135267.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77384
- Scheduled area: 10831.23 ha
- Eligible blocks (age class >= 40): 773835
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.38 MB
- Schedules: 0.92 MB
- Runs: 0.00 MB
- Total: 24.30 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
