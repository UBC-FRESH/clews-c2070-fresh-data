# WS4 tiled 30-m dataset — I3|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I3|BC|S21` (parent `I3|BC`)
- Tile / row / col: `I3` / 2 / 1
- Province: `BC`
- Centroid: 52.257630, -126.418995
- Allocated harvest: 87724.293365 m3
- Productive subcell area: 178548.510806 ha
- Committed geometry area: 248879.955041 ha
- Clipped inventory geometry: 248879.955041 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1452288
- Blocks: 796130
- Forest area: 130705.92 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74392
- Scheduled area: 12294.36 ha
- Eligible blocks (age class >= 40): 743918
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.30 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 22.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
