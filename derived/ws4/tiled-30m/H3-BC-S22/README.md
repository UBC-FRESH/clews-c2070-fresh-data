# WS4 tiled 30-m dataset — H3|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H3|BC|S22` (parent `H3|BC`)
- Tile / row / col: `H3` / 2 / 2
- Province: `BC`
- Centroid: 51.260962, -124.757569
- Allocated harvest: 91768.239037 m3
- Productive subcell area: 139257.618241 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 911997
- Blocks: 514994
- Forest area: 82079.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46021
- Scheduled area: 6794.82 ha
- Eligible blocks (age class >= 40): 460205
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.84 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 14.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
