# WS4 tiled 30-m dataset — N3|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N3|BC|S31` (parent `N3|BC`)
- Tile / row / col: `N3` / 3 / 1
- Province: `BC`
- Centroid: 58.529381, -133.095032
- Allocated harvest: 55418.590076 m3
- Productive subcell area: 127818.512069 ha
- Committed geometry area: 237633.969471 ha
- Clipped inventory geometry: 237633.969471 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 845161
- Blocks: 468454
- Forest area: 76064.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42208
- Scheduled area: 6446.25 ha
- Eligible blocks (age class >= 40): 422076
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.77 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 13.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
