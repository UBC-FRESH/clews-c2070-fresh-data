# WS4 tiled 30-m dataset — I24|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I24|QC|S12` (parent `I24|QC`)
- Tile / row / col: `I24` / 1 / 2
- Province: `QC`
- Centroid: 54.907253, -76.234339
- Allocated harvest: 16833.077766 m3
- Productive subcell area: 107048.282446 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1468883
- Blocks: 461524
- Forest area: 132199.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37634
- Scheduled area: 11042.91 ha
- Eligible blocks (age class >= 40): 376334
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.09 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 17.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
