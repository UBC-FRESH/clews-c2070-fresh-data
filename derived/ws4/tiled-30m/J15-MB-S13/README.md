# WS4 tiled 30-m dataset — J15|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J15|MB|S13` (parent `J15|MB`)
- Tile / row / col: `J15` / 1 / 3
- Province: `MB`
- Centroid: 57.849935, -97.347712
- Allocated harvest: 3228.639423 m3
- Productive subcell area: 155253.293299 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1837274
- Blocks: 368691
- Forest area: 165354.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30187
- Scheduled area: 13549.05 ha
- Eligible blocks (age class >= 40): 301867
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.23 MB
- Schedules: 0.35 MB
- Runs: 0.00 MB
- Total: 18.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
