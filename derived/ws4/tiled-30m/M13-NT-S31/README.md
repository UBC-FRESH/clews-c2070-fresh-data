# WS4 tiled 30-m dataset — M13|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M13|NT|S31` (parent `M13|NT`)
- Tile / row / col: `M13` / 3 / 1
- Province: `NT`
- Centroid: 62.531129, -105.784111
- Allocated harvest: 6.568828 m3
- Productive subcell area: 17160.748858 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 17161
- Blocks: 14525
- Forest area: 1544.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4090
- Scheduled area: 436.86 ha
- Eligible blocks (age class >= 40): 4090
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.47 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.51 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
