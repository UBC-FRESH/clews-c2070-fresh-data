# WS4 tiled 30-m dataset — O11|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O11|NT|S21` (parent `O11|NT`)
- Tile / row / col: `O11` / 2 / 1
- Province: `NT`
- Centroid: 64.166071, -112.964663
- Allocated harvest: 10.588826 m3
- Productive subcell area: 28178.568866 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 426427
- Blocks: 241613
- Forest area: 38378.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11336
- Scheduled area: 1662.21 ha
- Eligible blocks (age class >= 40): 113354
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.93 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 7.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
