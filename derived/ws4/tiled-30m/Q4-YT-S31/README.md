# WS4 tiled 30-m dataset — Q4|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q4|YT|S31` (parent `Q4|YT`)
- Tile / row / col: `Q4` / 3 / 1
- Province: `YT`
- Centroid: 62.716932, -135.737385
- Allocated harvest: 327.910389 m3
- Productive subcell area: 191647.548919 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2439152
- Blocks: 702008
- Forest area: 219523.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62991
- Scheduled area: 16734.15 ha
- Eligible blocks (age class >= 40): 629901
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.72 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 27.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
