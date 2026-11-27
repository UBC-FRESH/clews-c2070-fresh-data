# WS4 tiled 30-m dataset — L7|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|BC|S33` (parent `L7|BC`)
- Tile / row / col: `L7` / 3 / 3
- Province: `BC`
- Centroid: 59.211134, -120.061559
- Allocated harvest: 5215.559388 m3
- Productive subcell area: 12753.893496 ha
- Committed geometry area: 14890.324828 ha
- Clipped inventory geometry: 14890.324828 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 96652
- Blocks: 47156
- Forest area: 8698.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3999
- Scheduled area: 577.53 ha
- Eligible blocks (age class >= 40): 39990
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.76 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
