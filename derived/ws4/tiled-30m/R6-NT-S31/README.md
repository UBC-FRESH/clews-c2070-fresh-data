# WS4 tiled 30-m dataset — R6|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R6|NT|S31` (parent `R6|NT`)
- Tile / row / col: `R6` / 3 / 1
- Province: `NT`
- Centroid: 65.406255, -132.159169
- Allocated harvest: 33.876113 m3
- Productive subcell area: 49350.557111 ha
- Committed geometry area: 130350.518551 ha
- Clipped inventory geometry: 130350.518551 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 403195
- Blocks: 175059
- Forest area: 36287.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11272
- Scheduled area: 2092.50 ha
- Eligible blocks (age class >= 40): 112714
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.02 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 6.15 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
