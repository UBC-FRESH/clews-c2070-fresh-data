# WS4 tiled 30-m dataset — H6|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|BC|S31` (parent `H6|BC`)
- Tile / row / col: `H6` / 3 / 1
- Province: `BC`
- Centroid: 53.166812, -119.687336
- Allocated harvest: 81296.441242 m3
- Productive subcell area: 137839.411102 ha
- Committed geometry area: 231733.897485 ha
- Clipped inventory geometry: 231733.897485 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1577499
- Blocks: 854340
- Forest area: 141974.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 80042
- Scheduled area: 12414.33 ha
- Eligible blocks (age class >= 40): 800414
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.21 MB
- Schedules: 0.95 MB
- Runs: 0.00 MB
- Total: 24.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
