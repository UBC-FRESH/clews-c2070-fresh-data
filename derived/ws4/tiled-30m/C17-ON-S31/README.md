# WS4 tiled 30-m dataset — C17|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C17|ON|S31` (parent `C17|ON`)
- Tile / row / col: `C17` / 3 / 1
- Province: `ON`
- Centroid: 49.206264, -94.083175
- Allocated harvest: 31907.844808 m3
- Productive subcell area: 144614.921149 ha
- Committed geometry area: 187567.946974 ha
- Clipped inventory geometry: 187567.946974 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1650038
- Blocks: 790925
- Forest area: 148503.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73868
- Scheduled area: 13271.67 ha
- Eligible blocks (age class >= 40): 738676
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.93 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 23.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
