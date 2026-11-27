# WS4 tiled 30-m dataset — K6|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K6|BC|S13` (parent `K6|BC`)
- Tile / row / col: `K6` / 1 / 3
- Province: `BC`
- Centroid: 56.498430, -120.376790
- Allocated harvest: 90327.371594 m3
- Productive subcell area: 195957.432823 ha
- Committed geometry area: 228699.579608 ha
- Clipped inventory geometry: 228699.579608 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1754931
- Blocks: 706531
- Forest area: 157943.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58800
- Scheduled area: 11383.29 ha
- Eligible blocks (age class >= 40): 587996
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.18 MB
- Schedules: 0.70 MB
- Runs: 0.00 MB
- Total: 22.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
