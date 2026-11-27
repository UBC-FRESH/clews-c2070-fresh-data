# WS4 tiled 30-m dataset — J32|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|QC|S11` (parent `J32|QC`)
- Tile / row / col: `J32` / 1 / 1
- Province: `QC`
- Centroid: 51.760132, -59.296102
- Allocated harvest: 34474.114666 m3
- Productive subcell area: 170714.965468 ha
- Committed geometry area: 240341.393096 ha
- Clipped inventory geometry: 240341.393096 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2226578
- Blocks: 617192
- Forest area: 200392.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58093
- Scheduled area: 19384.29 ha
- Eligible blocks (age class >= 40): 580926
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.80 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 25.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
