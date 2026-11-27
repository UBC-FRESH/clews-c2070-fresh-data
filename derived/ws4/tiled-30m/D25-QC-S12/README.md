# WS4 tiled 30-m dataset — D25|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D25|QC|S12` (parent `D25|QC`)
- Tile / row / col: `D25` / 1 / 2
- Province: `QC`
- Centroid: 48.002667, -77.229546
- Allocated harvest: 70742.284250 m3
- Productive subcell area: 191269.768582 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2043399
- Blocks: 879599
- Forest area: 183905.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79626
- Scheduled area: 15936.75 ha
- Eligible blocks (age class >= 40): 796260
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.28 MB
- Schedules: 0.95 MB
- Runs: 0.00 MB
- Total: 28.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
