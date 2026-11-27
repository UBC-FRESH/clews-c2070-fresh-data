# WS4 tiled 30-m dataset — J11|SK|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J11|SK|S11` (parent `J11|SK`)
- Tile / row / col: `J11` / 1 / 1
- Province: `SK`
- Centroid: 57.010587, -109.205069
- Allocated harvest: 14280.168372 m3
- Productive subcell area: 160918.415101 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2012778
- Blocks: 314668
- Forest area: 181150.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15363
- Scheduled area: 2923.20 ha
- Eligible blocks (age class >= 40): 153630
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.76 MB
- Schedules: 0.18 MB
- Runs: 0.00 MB
- Total: 16.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
