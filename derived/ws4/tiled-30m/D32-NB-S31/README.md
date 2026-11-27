# WS4 tiled 30-m dataset — D32|NB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D32|NB|S31` (parent `D32|NB`)
- Tile / row / col: `D32` / 3 / 1
- Province: `NB`
- Centroid: 45.701425, -64.808565
- Allocated harvest: 25410.150355 m3
- Productive subcell area: 29208.329174 ha
- Committed geometry area: 36040.975528 ha
- Clipped inventory geometry: 36040.975528 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 338234
- Blocks: 114883
- Forest area: 30441.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9757
- Scheduled area: 2193.84 ha
- Eligible blocks (age class >= 40): 97565
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.78 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 4.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
