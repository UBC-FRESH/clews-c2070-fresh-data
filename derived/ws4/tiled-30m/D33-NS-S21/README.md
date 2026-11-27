# WS4 tiled 30-m dataset — D33|NS|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D33|NS|S21` (parent `D33|NS`)
- Tile / row / col: `D33` / 2 / 1
- Province: `NS`
- Centroid: 44.652851, -63.448295
- Allocated harvest: 21226.754118 m3
- Productive subcell area: 44071.293521 ha
- Committed geometry area: 53357.794301 ha
- Clipped inventory geometry: 53357.794301 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 415180
- Blocks: 142992
- Forest area: 37366.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11546
- Scheduled area: 2914.56 ha
- Eligible blocks (age class >= 40): 115452
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.67 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 5.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
