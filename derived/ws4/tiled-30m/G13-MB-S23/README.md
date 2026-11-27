# WS4 tiled 30-m dataset — G13|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G13|MB|S23` (parent `G13|MB`)
- Tile / row / col: `G13` / 2 / 3
- Province: `MB`
- Centroid: 53.999332, -101.583743
- Allocated harvest: 3652.232313 m3
- Productive subcell area: 77419.666421 ha
- Committed geometry area: 129886.177720 ha
- Clipped inventory geometry: 129886.177720 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 804610
- Blocks: 302647
- Forest area: 72414.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26302
- Scheduled area: 6260.49 ha
- Eligible blocks (age class >= 40): 263015
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.35 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 10.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
