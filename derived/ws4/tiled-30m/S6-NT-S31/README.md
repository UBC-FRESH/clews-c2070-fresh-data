# WS4 tiled 30-m dataset — S6|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S6|NT|S31` (parent `S6|NT`)
- Tile / row / col: `S6` / 3 / 1
- Province: `NT`
- Centroid: 66.579136, -133.650618
- Allocated harvest: 3.880017 m3
- Productive subcell area: 3801.612276 ha
- Committed geometry area: 6732.964633 ha
- Clipped inventory geometry: 6732.964633 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 21137
- Blocks: 5071
- Forest area: 1902.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 445
- Scheduled area: 64.80 ha
- Eligible blocks (age class >= 40): 445
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.33 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
