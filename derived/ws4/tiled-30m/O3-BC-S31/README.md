# WS4 tiled 30-m dataset — O3|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O3|BC|S31` (parent `O3|BC`)
- Tile / row / col: `O3` / 3 / 1
- Province: `BC`
- Centroid: 59.661219, -134.653815
- Allocated harvest: 55555.680086 m3
- Productive subcell area: 136482.869177 ha
- Committed geometry area: 246195.443820 ha
- Clipped inventory geometry: 246195.443820 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 945688
- Blocks: 556430
- Forest area: 85111.92 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50328
- Scheduled area: 7381.98 ha
- Eligible blocks (age class >= 40): 503272
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.53 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 15.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
