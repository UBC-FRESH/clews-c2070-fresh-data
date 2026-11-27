# WS4 tiled 30-m dataset — F3|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F3|BC|S32` (parent `F3|BC`)
- Tile / row / col: `F3` / 3 / 2
- Province: `BC`
- Centroid: 49.271810, -123.057792
- Allocated harvest: 80956.572330 m3
- Productive subcell area: 80638.777621 ha
- Committed geometry area: 119443.312211 ha
- Clipped inventory geometry: 119443.312211 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 606599
- Blocks: 366073
- Forest area: 54593.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33574
- Scheduled area: 4921.56 ha
- Eligible blocks (age class >= 40): 335731
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.84 MB
- Schedules: 0.39 MB
- Runs: 0.00 MB
- Total: 10.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
