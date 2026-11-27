# WS4 tiled 30-m dataset — O4|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O4|YT|S13` (parent `O4|YT`)
- Tile / row / col: `O4` / 1 / 3
- Province: `YT`
- Centroid: 60.196306, -129.805665
- Allocated harvest: 267.059224 m3
- Productive subcell area: 164166.799959 ha
- Committed geometry area: 219971.011543 ha
- Clipped inventory geometry: 219971.011543 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2305797
- Blocks: 1178465
- Forest area: 207521.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 116083
- Scheduled area: 20169.36 ha
- Eligible blocks (age class >= 40): 1160827
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 33.39 MB
- Schedules: 1.40 MB
- Runs: 0.00 MB
- Total: 34.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
