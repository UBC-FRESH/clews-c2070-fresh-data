# WS4 tiled 30-m dataset — P4|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P4|YT|S13` (parent `P4|YT`)
- Tile / row / col: `P4` / 1 / 3
- Province: `YT`
- Centroid: 61.341823, -131.315132
- Allocated harvest: 236.260843 m3
- Productive subcell area: 170296.639153 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1568936
- Blocks: 698642
- Forest area: 141204.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 56673
- Scheduled area: 11605.05 ha
- Eligible blocks (age class >= 40): 566725
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.23 MB
- Schedules: 0.67 MB
- Runs: 0.00 MB
- Total: 21.90 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
