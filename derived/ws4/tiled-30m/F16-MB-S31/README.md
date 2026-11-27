# WS4 tiled 30-m dataset — F16|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F16|MB|S31` (parent `F16|MB`)
- Tile / row / col: `F16` / 3 / 1
- Province: `MB`
- Centroid: 53.281931, -96.306933
- Allocated harvest: 7549.432927 m3
- Productive subcell area: 204111.368633 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2311658
- Blocks: 839525
- Forest area: 208049.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75810
- Scheduled area: 17061.03 ha
- Eligible blocks (age class >= 40): 758098
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.52 MB
- Schedules: 0.90 MB
- Runs: 0.00 MB
- Total: 29.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
