# WS4 tiled 30-m dataset — T8|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T8|NT|S31` (parent `T8|NT`)
- Tile / row / col: `T8` / 3 / 1
- Province: `NT`
- Centroid: 69.275543, -130.189055
- Allocated harvest: 5.130491 m3
- Productive subcell area: 11349.694128 ha
- Committed geometry area: 240872.778117 ha
- Clipped inventory geometry: 240872.778117 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 332802
- Blocks: 181801
- Forest area: 29952.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9511
- Scheduled area: 1324.44 ha
- Eligible blocks (age class >= 40): 95110
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.58 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 5.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
