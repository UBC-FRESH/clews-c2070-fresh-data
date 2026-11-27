# WS4 tiled 30-m dataset — C18|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C18|ON|S13` (parent `C18|ON`)
- Tile / row / col: `C18` / 1 / 3
- Province: `ON`
- Centroid: 48.299448, -90.750252
- Allocated harvest: 26519.868976 m3
- Productive subcell area: 122596.067626 ha
- Committed geometry area: 154262.344477 ha
- Clipped inventory geometry: 154262.344477 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1385526
- Blocks: 506455
- Forest area: 124697.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45488
- Scheduled area: 9005.40 ha
- Eligible blocks (age class >= 40): 454872
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.24 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 17.77 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
