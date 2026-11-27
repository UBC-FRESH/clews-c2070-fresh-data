# WS4 tiled 30-m dataset — J14|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J14|MB|S33` (parent `J14|MB`)
- Tile / row / col: `J14` / 3 / 3
- Province: `MB`
- Centroid: 58.689395, -100.068293
- Allocated harvest: 2702.992908 m3
- Productive subcell area: 149757.287733 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1616412
- Blocks: 407565
- Forest area: 145477.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25050
- Scheduled area: 8075.61 ha
- Eligible blocks (age class >= 40): 250493
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.78 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 17.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
