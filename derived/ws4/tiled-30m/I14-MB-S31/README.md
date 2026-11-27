# WS4 tiled 30-m dataset — I14|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I14|MB|S31` (parent `I14|MB`)
- Tile / row / col: `I14` / 3 / 1
- Province: `MB`
- Centroid: 57.229259, -101.555439
- Allocated harvest: 6054.099470 m3
- Productive subcell area: 182094.224631 ha
- Committed geometry area: 249404.499422 ha
- Clipped inventory geometry: 249404.499422 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1812802
- Blocks: 321527
- Forest area: 163152.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24808
- Scheduled area: 9689.04 ha
- Eligible blocks (age class >= 40): 248079
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.67 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 16.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
