# WS4 tiled 30-m dataset — C19|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C19|ON|S31` (parent `C19|ON`)
- Tile / row / col: `C19` / 3 / 1
- Province: `ON`
- Centroid: 49.084145, -90.009040
- Allocated harvest: 50942.946699 m3
- Productive subcell area: 208747.655292 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2440641
- Blocks: 778080
- Forest area: 219657.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65924
- Scheduled area: 14469.48 ha
- Eligible blocks (age class >= 40): 659233
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.31 MB
- Schedules: 0.78 MB
- Runs: 0.00 MB
- Total: 29.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
