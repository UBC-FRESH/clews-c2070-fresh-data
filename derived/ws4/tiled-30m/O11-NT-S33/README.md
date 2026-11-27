# WS4 tiled 30-m dataset — O11|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O11|NT|S33` (parent `O11|NT`)
- Tile / row / col: `O11` / 3 / 3
- Province: `NT`
- Centroid: 64.857551, -111.178812
- Allocated harvest: 10.588826 m3
- Productive subcell area: 28178.568866 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 82785
- Blocks: 62339
- Forest area: 7450.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2161
- Scheduled area: 215.55 ha
- Eligible blocks (age class >= 40): 21608
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.86 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
