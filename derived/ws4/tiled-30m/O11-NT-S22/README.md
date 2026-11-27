# WS4 tiled 30-m dataset — O11|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O11|NT|S22` (parent `O11|NT`)
- Tile / row / col: `O11` / 2 / 2
- Province: `NT`
- Centroid: 64.291434, -111.941681
- Allocated harvest: 10.588826 m3
- Productive subcell area: 28178.568866 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 49090
- Blocks: 39921
- Forest area: 4418.10 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1605
- Scheduled area: 171.45 ha
- Eligible blocks (age class >= 40): 16041
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.20 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
