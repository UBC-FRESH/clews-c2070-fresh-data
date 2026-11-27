# WS4 tiled 30-m dataset — D16|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D16|MB|S11` (parent `D16|MB`)
- Tile / row / col: `D16` / 1 / 1
- Province: `MB`
- Centroid: 49.655786, -96.192831
- Allocated harvest: 9236.567280 m3
- Productive subcell area: 176295.350705 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1944161
- Blocks: 698643
- Forest area: 174974.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60394
- Scheduled area: 14890.05 ha
- Eligible blocks (age class >= 40): 603933
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.88 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 24.60 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
