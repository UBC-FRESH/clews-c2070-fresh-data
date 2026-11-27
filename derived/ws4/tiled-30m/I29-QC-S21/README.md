# WS4 tiled 30-m dataset — I29|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I29|QC|S21` (parent `I29|QC`)
- Tile / row / col: `I29` / 2 / 1
- Province: `QC`
- Centroid: 52.885193, -66.310585
- Allocated harvest: 402.726927 m3
- Productive subcell area: 2210.246348 ha
- Committed geometry area: 3425.739991 ha
- Clipped inventory geometry: 3425.739991 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 15923
- Blocks: 5001
- Forest area: 1433.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4680
- Scheduled area: 1397.79 ha
- Eligible blocks (age class >= 40): 4680
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.28 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 0.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
