# WS4 tiled 30-m dataset — L5|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L5|BC|S13` (parent `L5|BC`)
- Tile / row / col: `L5` / 1 / 3
- Province: `BC`
- Centroid: 57.182611, -123.667443
- Allocated harvest: 41098.525057 m3
- Productive subcell area: 153152.440818 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1683887
- Blocks: 749380
- Forest area: 151549.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68595
- Scheduled area: 13746.69 ha
- Eligible blocks (age class >= 40): 685945
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.64 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 23.45 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
