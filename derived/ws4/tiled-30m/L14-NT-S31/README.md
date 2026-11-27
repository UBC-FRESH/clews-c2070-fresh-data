# WS4 tiled 30-m dataset — L14|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L14|NT|S31` (parent `L14|NT`)
- Tile / row / col: `L14` / 3 / 1
- Province: `NT`
- Centroid: 61.358808, -102.465079
- Allocated harvest: 29.791492 m3
- Productive subcell area: 76647.151307 ha
- Committed geometry area: 241453.280510 ha
- Clipped inventory geometry: 241453.280510 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 312960
- Blocks: 211674
- Forest area: 28166.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12272
- Scheduled area: 1638.36 ha
- Eligible blocks (age class >= 40): 122712
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.92 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 6.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
