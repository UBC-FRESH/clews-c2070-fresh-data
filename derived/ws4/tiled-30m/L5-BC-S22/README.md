# WS4 tiled 30-m dataset — L5|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L5|BC|S22` (parent `L5|BC`)
- Tile / row / col: `L5` / 2 / 2
- Province: `BC`
- Centroid: 57.390778, -124.805502
- Allocated harvest: 41098.525057 m3
- Productive subcell area: 153152.440818 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2022188
- Blocks: 802698
- Forest area: 181996.92 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74695
- Scheduled area: 15637.41 ha
- Eligible blocks (age class >= 40): 746944
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.32 MB
- Schedules: 0.89 MB
- Runs: 0.00 MB
- Total: 26.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
