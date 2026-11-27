# WS4 tiled 30-m dataset — P2|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P2|BC|S13` (parent `P2|BC`)
- Tile / row / col: `P2` / 1 / 3
- Province: `BC`
- Centroid: 59.818671, -136.010880
- Allocated harvest: 5988.321211 m3
- Productive subcell area: 18501.410857 ha
- Committed geometry area: 156899.442588 ha
- Clipped inventory geometry: 156899.442588 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 133408
- Blocks: 84135
- Forest area: 12006.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7054
- Scheduled area: 917.19 ha
- Eligible blocks (age class >= 40): 70532
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.81 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 2.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
