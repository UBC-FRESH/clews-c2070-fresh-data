# WS4 tiled 30-m dataset — N9|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N9|NT|S12` (parent `N9|NT`)
- Tile / row / col: `N9` / 1 / 2
- Province: `NT`
- Centroid: 61.696357, -116.556590
- Allocated harvest: 111.035828 m3
- Productive subcell area: 95511.724318 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 980905
- Blocks: 346869
- Forest area: 88281.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13692
- Scheduled area: 2123.46 ha
- Eligible blocks (age class >= 40): 136916
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.57 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 11.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
