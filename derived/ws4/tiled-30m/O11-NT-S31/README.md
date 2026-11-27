# WS4 tiled 30-m dataset — O11|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O11|NT|S31` (parent `O11|NT`)
- Tile / row / col: `O11` / 3 / 1
- Province: `NT`
- Centroid: 64.610065, -113.264977
- Allocated harvest: 10.588826 m3
- Productive subcell area: 28178.568866 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 241828
- Blocks: 145906
- Forest area: 21764.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5871
- Scheduled area: 817.38 ha
- Eligible blocks (age class >= 40): 58702
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.53 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 4.60 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
