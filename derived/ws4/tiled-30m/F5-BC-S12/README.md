# WS4 tiled 30-m dataset — F5|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F5|BC|S12` (parent `F5|BC`)
- Tile / row / col: `F5` / 1 / 2
- Province: `BC`
- Centroid: 49.482482, -118.864926
- Allocated harvest: 161914.105795 m3
- Productive subcell area: 203427.507706 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2562869
- Blocks: 1088582
- Forest area: 230658.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 97619
- Scheduled area: 15427.98 ha
- Eligible blocks (age class >= 40): 976188
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 33.38 MB
- Schedules: 1.17 MB
- Runs: 0.00 MB
- Total: 34.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
