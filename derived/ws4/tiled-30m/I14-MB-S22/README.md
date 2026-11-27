# WS4 tiled 30-m dataset — I14|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I14|MB|S22` (parent `I14|MB`)
- Tile / row / col: `I14` / 2 / 2
- Province: `MB`
- Centroid: 56.816045, -100.636783
- Allocated harvest: 6068.554782 m3
- Productive subcell area: 182529.009153 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1907098
- Blocks: 268741
- Forest area: 171638.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20144
- Scheduled area: 6806.88 ha
- Eligible blocks (age class >= 40): 201436
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.38 MB
- Schedules: 0.23 MB
- Runs: 0.00 MB
- Total: 16.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
