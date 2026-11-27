# WS4 tiled 30-m dataset — I14|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I14|MB|S11` (parent `I14|MB`)
- Tile / row / col: `I14` / 1 / 1
- Province: `MB`
- Centroid: 56.315407, -101.386519
- Allocated harvest: 6068.554782 m3
- Productive subcell area: 182529.009153 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1816095
- Blocks: 308559
- Forest area: 163448.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20947
- Scheduled area: 6614.28 ha
- Eligible blocks (age class >= 40): 209462
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.45 MB
- Schedules: 0.24 MB
- Runs: 0.00 MB
- Total: 16.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
