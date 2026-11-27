# WS4 tiled 30-m dataset — J2|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J2|BC|S12` (parent `J2|BC`)
- Tile / row / col: `J2` / 1 / 2
- Province: `BC`
- Centroid: 52.626801, -128.429288
- Allocated harvest: 95354.056875 m3
- Productive subcell area: 125695.479235 ha
- Committed geometry area: 172150.460271 ha
- Clipped inventory geometry: 172150.460271 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1787776
- Blocks: 844165
- Forest area: 160899.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 83625
- Scheduled area: 15664.59 ha
- Eligible blocks (age class >= 40): 836243
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.25 MB
- Schedules: 0.99 MB
- Runs: 0.00 MB
- Total: 25.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
