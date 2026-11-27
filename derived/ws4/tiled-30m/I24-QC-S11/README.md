# WS4 tiled 30-m dataset — I24|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I24|QC|S11` (parent `I24|QC`)
- Tile / row / col: `I24` / 1 / 1
- Province: `QC`
- Centroid: 55.037733, -76.997132
- Allocated harvest: 16833.077766 m3
- Productive subcell area: 107048.282446 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1651265
- Blocks: 449714
- Forest area: 148613.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36740
- Scheduled area: 16198.74 ha
- Eligible blocks (age class >= 40): 367400
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.98 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 18.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
