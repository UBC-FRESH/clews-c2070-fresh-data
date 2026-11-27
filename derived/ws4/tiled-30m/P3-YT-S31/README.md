# WS4 tiled 30-m dataset — P3|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P3|YT|S31` (parent `P3|YT`)
- Tile / row / col: `P3` / 3 / 1
- Province: `YT`
- Centroid: 60.774619, -136.316341
- Allocated harvest: 294.422955 m3
- Productive subcell area: 165254.462030 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1795544
- Blocks: 839688
- Forest area: 161598.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73845
- Scheduled area: 14362.29 ha
- Eligible blocks (age class >= 40): 738443
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.66 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 25.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
