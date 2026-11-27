# WS4 tiled 30-m dataset — N6|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|NT|S12` (parent `N6|NT`)
- Tile / row / col: `N6` / 1 / 2
- Province: `NT`
- Centroid: 60.207253, -124.065670
- Allocated harvest: 10.714831 m3
- Productive subcell area: 7282.219559 ha
- Committed geometry area: 9218.405835 ha
- Clipped inventory geometry: 9218.405835 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 87936
- Blocks: 41707
- Forest area: 7914.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3913
- Scheduled area: 699.84 ha
- Eligible blocks (age class >= 40): 39127
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.60 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
