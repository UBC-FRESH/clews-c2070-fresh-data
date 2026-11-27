# WS4 tiled 30-m dataset — V6|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `V6|YT|S31` (parent `V6|YT`)
- Tile / row / col: `V6` / 3 / 1
- Province: `YT`
- Centroid: 69.636139, -140.990392
- Allocated harvest: 0.018043 m3
- Productive subcell area: 15.628339 ha
- Committed geometry area: 358.574834 ha
- Clipped inventory geometry: 358.574834 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1
- Blocks: 1
- Forest area: 0.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 0
- Scheduled area: 0.00 ha
- Eligible blocks (age class >= 40): 0
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.07 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
