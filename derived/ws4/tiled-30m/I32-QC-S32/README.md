# WS4 tiled 30-m dataset — I32|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I32|QC|S32` (parent `I32|QC`)
- Tile / row / col: `I32` / 3 / 2
- Province: `QC`
- Centroid: 51.156553, -59.088908
- Allocated harvest: 38072.836007 m3
- Productive subcell area: 163251.935827 ha
- Committed geometry area: 231838.688153 ha
- Clipped inventory geometry: 231838.688153 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1551065
- Blocks: 625792
- Forest area: 139595.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57260
- Scheduled area: 13300.47 ha
- Eligible blocks (age class >= 40): 572600
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.15 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 20.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
