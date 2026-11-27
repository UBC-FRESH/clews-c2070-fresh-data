# WS4 tiled 30-m dataset — O4|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O4|YT|S12` (parent `O4|YT`)
- Tile / row / col: `O4` / 1 / 2
- Province: `YT`
- Centroid: 60.081116, -130.607461
- Allocated harvest: 92.377446 m3
- Productive subcell area: 56786.316813 ha
- Committed geometry area: 76089.340562 ha
- Clipped inventory geometry: 76089.340562 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 589556
- Blocks: 347448
- Forest area: 53060.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32344
- Scheduled area: 4740.30 ha
- Eligible blocks (age class >= 40): 323433
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.46 MB
- Schedules: 0.38 MB
- Runs: 0.00 MB
- Total: 9.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
