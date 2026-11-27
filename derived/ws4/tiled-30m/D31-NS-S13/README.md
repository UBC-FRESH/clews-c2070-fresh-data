# WS4 tiled 30-m dataset — D31|NS|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D31|NS|S13` (parent `D31|NS`)
- Tile / row / col: `D31` / 1 / 3
- Province: `NS`
- Centroid: 44.730924, -65.656812
- Allocated harvest: 4841.518160 m3
- Productive subcell area: 7699.998788 ha
- Committed geometry area: 9506.934998 ha
- Clipped inventory geometry: 9506.934998 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 96147
- Blocks: 26695
- Forest area: 8653.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2335
- Scheduled area: 775.98 ha
- Eligible blocks (age class >= 40): 23342
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.37 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
