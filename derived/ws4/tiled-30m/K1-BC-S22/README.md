# WS4 tiled 30-m dataset — K1|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K1|BC|S22` (parent `K1|BC`)
- Tile / row / col: `K1` / 2 / 2
- Province: `BC`
- Centroid: 53.446279, -132.124773
- Allocated harvest: 115945.571805 m3
- Productive subcell area: 123499.476897 ha
- Committed geometry area: 131898.391133 ha
- Clipped inventory geometry: 131898.391133 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1402195
- Blocks: 525461
- Forest area: 126197.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51906
- Scheduled area: 10254.15 ha
- Eligible blocks (age class >= 40): 519057
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.18 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 17.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
