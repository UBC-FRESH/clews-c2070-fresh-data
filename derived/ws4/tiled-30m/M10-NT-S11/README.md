# WS4 tiled 30-m dataset — M10|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M10|NT|S11` (parent `M10|NT`)
- Tile / row / col: `M10` / 1 / 1
- Province: `NT`
- Centroid: 60.667509, -113.840612
- Allocated harvest: 165.218418 m3
- Productive subcell area: 123265.143318 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1621940
- Blocks: 697413
- Forest area: 145974.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 54344
- Scheduled area: 10736.28 ha
- Eligible blocks (age class >= 40): 543439
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.21 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 21.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
