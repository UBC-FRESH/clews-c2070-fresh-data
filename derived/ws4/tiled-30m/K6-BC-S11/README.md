# WS4 tiled 30-m dataset — K6|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K6|BC|S11` (parent `K6|BC`)
- Tile / row / col: `K6` / 1 / 1
- Province: `BC`
- Centroid: 56.127681, -121.853743
- Allocated harvest: 98740.202921 m3
- Productive subcell area: 214208.343932 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2458315
- Blocks: 953416
- Forest area: 221248.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 90646
- Scheduled area: 19782.00 ha
- Eligible blocks (age class >= 40): 906459
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.07 MB
- Schedules: 1.08 MB
- Runs: 0.00 MB
- Total: 32.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
