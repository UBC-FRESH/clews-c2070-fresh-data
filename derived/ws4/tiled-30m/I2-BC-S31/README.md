# WS4 tiled 30-m dataset — I2|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I2|BC|S31` (parent `I2|BC`)
- Tile / row / col: `I2` / 3 / 1
- Province: `BC`
- Centroid: 51.965089, -128.446458
- Allocated harvest: 2116.150167 m3
- Productive subcell area: 2876.103816 ha
- Committed geometry area: 4239.295355 ha
- Clipped inventory geometry: 4239.295355 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 44429
- Blocks: 22664
- Forest area: 3998.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2246
- Scheduled area: 401.94 ha
- Eligible blocks (age class >= 40): 22458
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.85 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.87 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
