# WS4 tiled 30-m dataset — M13|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M13|NT|S21` (parent `M13|NT`)
- Tile / row / col: `M13` / 2 / 1
- Province: `NT`
- Centroid: 62.075157, -105.617734
- Allocated harvest: 6.568828 m3
- Productive subcell area: 17160.748858 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 81082
- Blocks: 62709
- Forest area: 7297.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2365
- Scheduled area: 250.20 ha
- Eligible blocks (age class >= 40): 23649
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.90 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
