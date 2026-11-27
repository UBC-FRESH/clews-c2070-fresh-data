# WS4 tiled 30-m dataset — I24|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I24|QC|S32` (parent `I24|QC`)
- Tile / row / col: `I24` / 3 / 2
- Province: `QC`
- Centroid: 55.782995, -75.761077
- Allocated harvest: 16833.077766 m3
- Productive subcell area: 107048.282446 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1396700
- Blocks: 620689
- Forest area: 125703.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50405
- Scheduled area: 10502.64 ha
- Eligible blocks (age class >= 40): 504045
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.49 MB
- Schedules: 0.60 MB
- Runs: 0.00 MB
- Total: 19.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
