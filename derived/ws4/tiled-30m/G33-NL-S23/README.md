# WS4 tiled 30-m dataset — G33|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G33|NL|S23` (parent `G33|NL`)
- Tile / row / col: `G33` / 2 / 3
- Province: `NL`
- Centroid: 47.653116, -59.153398
- Allocated harvest: 1327.806923 m3
- Productive subcell area: 22467.576694 ha
- Committed geometry area: 36472.885904 ha
- Clipped inventory geometry: 36472.885904 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 203987
- Blocks: 98698
- Forest area: 18358.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8042
- Scheduled area: 1602.90 ha
- Eligible blocks (age class >= 40): 80419
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.55 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 3.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
