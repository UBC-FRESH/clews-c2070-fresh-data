# WS4 tiled 30-m dataset — J2|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J2|BC|S11` (parent `J2|BC`)
- Tile / row / col: `J2` / 1 / 1
- Province: `BC`
- Centroid: 52.555449, -129.009847
- Allocated harvest: 18178.880985 m3
- Productive subcell area: 23963.355438 ha
- Committed geometry area: 32819.817335 ha
- Clipped inventory geometry: 32819.817335 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 351206
- Blocks: 145084
- Forest area: 31608.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14423
- Scheduled area: 3304.08 ha
- Eligible blocks (age class >= 40): 144223
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.23 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 5.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
