# WS4 tiled 30-m dataset — I24|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I24|QC|S33` (parent `I24|QC`)
- Tile / row / col: `I24` / 3 / 3
- Province: `QC`
- Centroid: 55.643745, -74.987200
- Allocated harvest: 16833.077766 m3
- Productive subcell area: 107048.282446 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1876283
- Blocks: 691424
- Forest area: 168865.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58656
- Scheduled area: 14379.84 ha
- Eligible blocks (age class >= 40): 586557
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.50 MB
- Schedules: 0.70 MB
- Runs: 0.00 MB
- Total: 23.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
