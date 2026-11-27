# WS4 tiled 30-m dataset — H24|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H24|QC|S21` (parent `H24|QC`)
- Tile / row / col: `H24` / 2 / 1
- Province: `QC`
- Centroid: 54.158518, -77.431942
- Allocated harvest: 27409.990069 m3
- Productive subcell area: 129578.173407 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1390924
- Blocks: 328780
- Forest area: 125183.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16883
- Scheduled area: 3600.18 ha
- Eligible blocks (age class >= 40): 168823
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.19 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 14.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
