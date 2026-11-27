# WS4 tiled 30-m dataset — F34|NS|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F34|NS|S21` (parent `F34|NS`)
- Tile / row / col: `F34` / 2 / 1
- Province: `NS`
- Centroid: 46.092095, -60.003323
- Allocated harvest: 14595.801417 m3
- Productive subcell area: 50774.471203 ha
- Committed geometry area: 63062.461819 ha
- Clipped inventory geometry: 63062.461819 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 513843
- Blocks: 203381
- Forest area: 46245.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17144
- Scheduled area: 3677.40 ha
- Eligible blocks (age class >= 40): 171435
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.14 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 7.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
