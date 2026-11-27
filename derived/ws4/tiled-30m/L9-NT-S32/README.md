# WS4 tiled 30-m dataset — L9|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L9|NT|S32` (parent `L9|NT`)
- Tile / row / col: `L9` / 3 / 2
- Province: `NT`
- Centroid: 60.088840, -115.355250
- Allocated harvest: 90.831901 m3
- Productive subcell area: 59794.952350 ha
- Committed geometry area: 94652.480641 ha
- Clipped inventory geometry: 94652.480641 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 708971
- Blocks: 229598
- Forest area: 63807.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18908
- Scheduled area: 4935.78 ha
- Eligible blocks (age class >= 40): 189071
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.38 MB
- Schedules: 0.22 MB
- Runs: 0.00 MB
- Total: 8.60 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
