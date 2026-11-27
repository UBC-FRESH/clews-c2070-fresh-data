# WS4 tiled 30-m dataset — O8|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O8|NT|S13` (parent `O8|NT`)
- Tile / row / col: `O8` / 1 / 3
- Province: `NT`
- Centroid: 62.666926, -119.458461
- Allocated harvest: 124.606406 m3
- Productive subcell area: 146971.298125 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1070831
- Blocks: 292793
- Forest area: 96374.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10138
- Scheduled area: 1716.48 ha
- Eligible blocks (age class >= 40): 101372
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.38 MB
- Schedules: 0.12 MB
- Runs: 0.00 MB
- Total: 11.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
