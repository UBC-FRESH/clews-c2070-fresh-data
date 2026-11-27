# WS4 tiled 30-m dataset — J4|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J4|BC|S11` (parent `J4|BC`)
- Tile / row / col: `J4` / 1 / 1
- Province: `BC`
- Centroid: 53.700071, -125.118788
- Allocated harvest: 113986.006079 m3
- Productive subcell area: 218265.682259 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2426110
- Blocks: 556335
- Forest area: 218349.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45386
- Scheduled area: 7861.86 ha
- Eligible blocks (age class >= 40): 453854
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.42 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 23.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
