# WS4 tiled 30-m dataset — E13|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E13|SK|S13` (parent `E13|SK`)
- Tile / row / col: `E13` / 1 / 3
- Province: `SK`
- Centroid: 50.823299, -101.555046
- Allocated harvest: 850.311587 m3
- Productive subcell area: 3864.259436 ha
- Committed geometry area: 28102.101822 ha
- Clipped inventory geometry: 28102.101822 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 24046
- Blocks: 7869
- Forest area: 2164.14 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4220
- Scheduled area: 1590.03 ha
- Eligible blocks (age class >= 40): 4220
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.40 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
