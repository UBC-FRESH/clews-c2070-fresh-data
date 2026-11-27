# WS4 tiled 30-m dataset — F12|SK|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F12|SK|S21` (parent `F12|SK`)
- Tile / row / col: `F12` / 2 / 1
- Province: `SK`
- Centroid: 52.331772, -105.223726
- Allocated harvest: 8837.586921 m3
- Productive subcell area: 42657.637342 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 116148
- Blocks: 59003
- Forest area: 10453.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3349
- Scheduled area: 683.73 ha
- Eligible blocks (age class >= 40): 33484
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.11 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 2.15 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
