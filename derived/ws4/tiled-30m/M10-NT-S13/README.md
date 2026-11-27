# WS4 tiled 30-m dataset — M10|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M10|NT|S13` (parent `M10|NT`)
- Tile / row / col: `M10` / 1 / 3
- Province: `NT`
- Centroid: 60.924632, -112.024252
- Allocated harvest: 165.218418 m3
- Productive subcell area: 123265.143318 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1035680
- Blocks: 507416
- Forest area: 93211.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21718
- Scheduled area: 3307.50 ha
- Eligible blocks (age class >= 40): 217177
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.10 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 14.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
