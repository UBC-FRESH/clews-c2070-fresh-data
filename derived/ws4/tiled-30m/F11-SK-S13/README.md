# WS4 tiled 30-m dataset — F11|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F11|SK|S13` (parent `F11|SK`)
- Tile / row / col: `F11` / 1 / 3
- Province: `SK`
- Centroid: 51.808887, -105.829337
- Allocated harvest: 1159.666907 m3
- Productive subcell area: 7873.844258 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 29379
- Blocks: 17515
- Forest area: 2644.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4476
- Scheduled area: 819.63 ha
- Eligible blocks (age class >= 40): 4476
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.62 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 0.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
