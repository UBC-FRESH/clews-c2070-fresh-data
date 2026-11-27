# WS4 tiled 30-m dataset — J4|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J4|BC|S31` (parent `J4|BC`)
- Tile / row / col: `J4` / 3 / 1
- Province: `BC`
- Centroid: 54.510823, -125.835556
- Allocated harvest: 113986.006079 m3
- Productive subcell area: 218265.682259 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2473868
- Blocks: 886622
- Forest area: 222648.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79953
- Scheduled area: 14768.19 ha
- Eligible blocks (age class >= 40): 799524
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.02 MB
- Schedules: 0.95 MB
- Runs: 0.00 MB
- Total: 30.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
