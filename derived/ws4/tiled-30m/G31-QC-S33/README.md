# WS4 tiled 30-m dataset — G31|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G31|QC|S33` (parent `G31|QC`)
- Tile / row / col: `G31` / 3 / 3
- Province: `QC`
- Centroid: 49.303135, -62.449475
- Allocated harvest: 80500.988206 m3
- Productive subcell area: 179295.226954 ha
- Committed geometry area: 210443.852163 ha
- Clipped inventory geometry: 210443.852163 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1815673
- Blocks: 969347
- Forest area: 163410.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 89722
- Scheduled area: 16406.19 ha
- Eligible blocks (age class >= 40): 897220
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.01 MB
- Schedules: 1.07 MB
- Runs: 0.00 MB
- Total: 27.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
