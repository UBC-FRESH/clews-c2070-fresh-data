# WS4 tiled 30-m dataset — N5|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|YT|S32` (parent `N5|YT`)
- Tile / row / col: `N5` / 3 / 2
- Province: `YT`
- Centroid: 60.245452, -127.738770
- Allocated harvest: 498.803320 m3
- Productive subcell area: 211178.008193 ha
- Committed geometry area: 241543.149882 ha
- Clipped inventory geometry: 241543.149882 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2503794
- Blocks: 889833
- Forest area: 225341.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 85822
- Scheduled area: 17863.38 ha
- Eligible blocks (age class >= 40): 858218
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.90 MB
- Schedules: 1.02 MB
- Runs: 0.00 MB
- Total: 29.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
