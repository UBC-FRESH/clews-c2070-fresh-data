# WS4 tiled 30-m dataset — N13|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N13|NT|S23` (parent `N13|NT`)
- Tile / row / col: `N13` / 2 / 3
- Province: `NT`
- Centroid: 63.589113, -104.086770
- Allocated harvest: 2.312004 m3
- Productive subcell area: 6489.910079 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 55195
- Blocks: 34947
- Forest area: 4967.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1639
- Scheduled area: 246.60 ha
- Eligible blocks (age class >= 40): 16386
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.17 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
