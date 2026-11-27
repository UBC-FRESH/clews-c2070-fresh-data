# WS4 tiled 30-m dataset — J15|MB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J15|MB|S12` (parent `J15|MB`)
- Tile / row / col: `J15` / 1 / 2
- Province: `MB`
- Centroid: 57.829827, -98.210140
- Allocated harvest: 3228.639423 m3
- Productive subcell area: 155253.293299 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1608613
- Blocks: 392959
- Forest area: 144775.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28451
- Scheduled area: 8497.35 ha
- Eligible blocks (age class >= 40): 284510
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.97 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 17.30 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
