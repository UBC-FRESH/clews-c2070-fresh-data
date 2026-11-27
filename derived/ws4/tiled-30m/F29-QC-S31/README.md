# WS4 tiled 30-m dataset — F29|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F29|QC|S31` (parent `F29|QC`)
- Tile / row / col: `F29` / 3 / 1
- Province: `QC`
- Centroid: 49.692175, -68.321192
- Allocated harvest: 96661.650003 m3
- Productive subcell area: 209879.138111 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2370118
- Blocks: 970186
- Forest area: 213310.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 86306
- Scheduled area: 16892.55 ha
- Eligible blocks (age class >= 40): 863051
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.50 MB
- Schedules: 1.03 MB
- Runs: 0.00 MB
- Total: 31.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
