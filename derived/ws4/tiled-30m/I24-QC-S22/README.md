# WS4 tiled 30-m dataset — I24|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I24|QC|S22` (parent `I24|QC`)
- Tile / row / col: `I24` / 2 / 2
- Province: `QC`
- Centroid: 55.345161, -76.000567
- Allocated harvest: 16833.077766 m3
- Productive subcell area: 107048.282446 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1338315
- Blocks: 580201
- Forest area: 120448.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49587
- Scheduled area: 10308.33 ha
- Eligible blocks (age class >= 40): 495863
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.62 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 18.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
