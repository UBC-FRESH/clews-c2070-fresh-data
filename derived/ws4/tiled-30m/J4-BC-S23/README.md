# WS4 tiled 30-m dataset — J4|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J4|BC|S23` (parent `J4|BC`)
- Tile / row / col: `J4` / 2 / 3
- Province: `BC`
- Centroid: 54.518315, -124.078097
- Allocated harvest: 113986.006079 m3
- Productive subcell area: 218265.682259 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2317200
- Blocks: 838528
- Forest area: 208548.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73766
- Scheduled area: 13986.54 ha
- Eligible blocks (age class >= 40): 737656
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.00 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 28.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
