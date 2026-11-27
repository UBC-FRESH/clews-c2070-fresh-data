# WS4 tiled 30-m dataset — P3|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P3|YT|S11` (parent `P3|YT`)
- Tile / row / col: `P3` / 1 / 1
- Province: `YT`
- Centroid: 60.124578, -135.214282
- Allocated harvest: 173.660301 m3
- Productive subcell area: 97472.493855 ha
- Committed geometry area: 147458.187600 ha
- Clipped inventory geometry: 147458.187600 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 440573
- Blocks: 262845
- Forest area: 39651.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23370
- Scheduled area: 3532.68 ha
- Eligible blocks (age class >= 40): 233694
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.41 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 7.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
