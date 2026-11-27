# WS4 tiled 30-m dataset — J11|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J11|AB|S31` (parent `J11|AB`)
- Tile / row / col: `J11` / 3 / 1
- Province: `AB`
- Centroid: 58.001703, -110.036666
- Allocated harvest: 1196.759791 m3
- Productive subcell area: 6600.033561 ha
- Committed geometry area: 8868.390474 ha
- Clipped inventory geometry: 8868.390474 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 65942
- Blocks: 11865
- Forest area: 5934.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 577
- Scheduled area: 97.20 ha
- Eligible blocks (age class >= 40): 5767
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.77 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.78 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
