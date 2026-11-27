# WS4 tiled 30-m dataset — F7|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F7|BC|S22` (parent `F7|BC`)
- Tile / row / col: `F7` / 2 / 2
- Province: `BC`
- Centroid: 50.643331, -115.353478
- Allocated harvest: 8251.593655 m3
- Productive subcell area: 12449.862840 ha
- Committed geometry area: 18159.812144 ha
- Clipped inventory geometry: 18159.812144 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 98647
- Blocks: 58952
- Forest area: 8878.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5437
- Scheduled area: 786.42 ha
- Eligible blocks (age class >= 40): 54366
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.02 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 2.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
