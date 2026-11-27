# WS4 tiled 30-m dataset — D15|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D15|MB|S33` (parent `D15|MB`)
- Tile / row / col: `D15` / 3 / 3
- Province: `MB`
- Centroid: 50.547198, -96.928812
- Allocated harvest: 1147.881972 m3
- Productive subcell area: 26936.761457 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 460839
- Blocks: 140818
- Forest area: 41475.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9492
- Scheduled area: 3147.03 ha
- Eligible blocks (age class >= 40): 94916
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.94 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 6.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
