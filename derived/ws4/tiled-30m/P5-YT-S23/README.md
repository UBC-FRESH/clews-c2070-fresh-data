# WS4 tiled 30-m dataset — P5|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P5|YT|S23` (parent `P5|YT`)
- Tile / row / col: `P5` / 2 / 3
- Province: `YT`
- Centroid: 62.424448, -129.551050
- Allocated harvest: 91.668414 m3
- Productive subcell area: 90797.113832 ha
- Committed geometry area: 128355.250789 ha
- Clipped inventory geometry: 128355.250789 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 819437
- Blocks: 355492
- Forest area: 73749.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29507
- Scheduled area: 6104.16 ha
- Eligible blocks (age class >= 40): 295067
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.12 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 11.47 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
