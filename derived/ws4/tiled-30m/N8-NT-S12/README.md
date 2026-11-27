# WS4 tiled 30-m dataset — N8|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N8|NT|S12` (parent `N8|NT`)
- Tile / row / col: `N8` / 1 / 2
- Province: `NT`
- Centroid: 61.207402, -119.268368
- Allocated harvest: 173.224674 m3
- Productive subcell area: 141366.160040 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1322616
- Blocks: 539444
- Forest area: 119035.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43872
- Scheduled area: 8824.68 ha
- Eligible blocks (age class >= 40): 438719
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.08 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 17.60 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
