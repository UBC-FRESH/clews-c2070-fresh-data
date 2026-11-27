# WS4 tiled 30-m dataset — Q3|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q3|YT|S23` (parent `Q3|YT`)
- Tile / row / col: `Q3` / 2 / 3
- Province: `YT`
- Centroid: 62.069541, -135.938747
- Allocated harvest: 255.809910 m3
- Productive subcell area: 171969.252036 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2378212
- Blocks: 959697
- Forest area: 214039.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 86876
- Scheduled area: 18473.31 ha
- Eligible blocks (age class >= 40): 868758
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.53 MB
- Schedules: 1.03 MB
- Runs: 0.00 MB
- Total: 31.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
