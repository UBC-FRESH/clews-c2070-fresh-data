# WS4 tiled 30-m dataset — H6|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|BC|S11` (parent `H6|BC`)
- Tile / row / col: `H6` / 1 / 1
- Province: `BC`
- Centroid: 52.340391, -119.115705
- Allocated harvest: 87704.520276 m3
- Productive subcell area: 148704.411178 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1687554
- Blocks: 833087
- Forest area: 151879.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77701
- Scheduled area: 13195.44 ha
- Eligible blocks (age class >= 40): 777004
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.29 MB
- Schedules: 0.92 MB
- Runs: 0.00 MB
- Total: 24.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
