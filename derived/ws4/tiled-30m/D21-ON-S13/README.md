# WS4 tiled 30-m dataset — D21|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D21|ON|S13` (parent `D21|ON`)
- Tile / row / col: `D21` / 1 / 3
- Province: `ON`
- Centroid: 49.093133, -84.486501
- Allocated harvest: 43833.125097 m3
- Productive subcell area: 223173.850989 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2376914
- Blocks: 872353
- Forest area: 213922.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76071
- Scheduled area: 15732.45 ha
- Eligible blocks (age class >= 40): 760701
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.35 MB
- Schedules: 0.90 MB
- Runs: 0.00 MB
- Total: 30.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
