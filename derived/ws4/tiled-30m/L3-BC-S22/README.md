# WS4 tiled 30-m dataset — L3|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L3|BC|S22` (parent `L3|BC`)
- Tile / row / col: `L3` / 2 / 2
- Province: `BC`
- Centroid: 56.060733, -129.199502
- Allocated harvest: 78650.339833 m3
- Productive subcell area: 142461.480316 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2062881
- Blocks: 886718
- Forest area: 185659.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 85613
- Scheduled area: 16327.26 ha
- Eligible blocks (age class >= 40): 856129
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.59 MB
- Schedules: 1.02 MB
- Runs: 0.00 MB
- Total: 27.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
