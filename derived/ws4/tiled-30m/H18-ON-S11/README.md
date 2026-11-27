# WS4 tiled 30-m dataset — H18|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H18|ON|S11` (parent `H18|ON`)
- Tile / row / col: `H18` / 1 / 1
- Province: `ON`
- Centroid: 55.025984, -91.499330
- Allocated harvest: 7666.324717 m3
- Productive subcell area: 95847.357376 ha
- Committed geometry area: 181911.778508 ha
- Clipped inventory geometry: 181911.778508 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1440925
- Blocks: 617366
- Forest area: 129683.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57196
- Scheduled area: 11157.57 ha
- Eligible blocks (age class >= 40): 571957
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.16 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 19.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
