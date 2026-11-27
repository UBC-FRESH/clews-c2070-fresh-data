# WS4 tiled 30-m dataset — O5|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O5|YT|S33` (parent `O5|YT`)
- Tile / row / col: `O5` / 3 / 3
- Province: `YT`
- Centroid: 61.652395, -128.378698
- Allocated harvest: 227.516387 m3
- Productive subcell area: 152077.548091 ha
- Committed geometry area: 220002.632464 ha
- Clipped inventory geometry: 220002.632464 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1020586
- Blocks: 464212
- Forest area: 91852.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38837
- Scheduled area: 8025.12 ha
- Eligible blocks (age class >= 40): 388370
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.95 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 14.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
