# WS4 tiled 30-m dataset — N5|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|YT|S31` (parent `N5|YT`)
- Tile / row / col: `N5` / 3 / 1
- Province: `YT`
- Centroid: 60.114151, -128.570161
- Allocated harvest: 265.746078 m3
- Productive subcell area: 112508.728813 ha
- Committed geometry area: 128686.282152 ha
- Clipped inventory geometry: 128686.282152 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1333394
- Blocks: 776640
- Forest area: 120005.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76642
- Scheduled area: 11231.64 ha
- Eligible blocks (age class >= 40): 766415
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.47 MB
- Schedules: 0.91 MB
- Runs: 0.00 MB
- Total: 21.37 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
