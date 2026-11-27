# WS4 tiled 30-m dataset — D24|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D24|ON|S11` (parent `D24|ON`)
- Tile / row / col: `D24` / 1 / 1
- Province: `ON`
- Centroid: 48.457917, -79.841710
- Allocated harvest: 44190.115393 m3
- Productive subcell area: 212688.379502 ha
- Committed geometry area: 237754.400593 ha
- Clipped inventory geometry: 237754.400593 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2288184
- Blocks: 882250
- Forest area: 205936.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79304
- Scheduled area: 16059.42 ha
- Eligible blocks (age class >= 40): 793033
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.76 MB
- Schedules: 0.94 MB
- Runs: 0.00 MB
- Total: 29.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
