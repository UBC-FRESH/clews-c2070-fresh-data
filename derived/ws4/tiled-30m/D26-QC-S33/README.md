# WS4 tiled 30-m dataset — D26|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D26|QC|S33` (parent `D26|QC`)
- Tile / row / col: `D26` / 3 / 3
- Province: `QC`
- Centroid: 48.324087, -74.272107
- Allocated harvest: 98164.902614 m3
- Productive subcell area: 206083.057949 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2241062
- Blocks: 782869
- Forest area: 201695.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 67518
- Scheduled area: 16045.29 ha
- Eligible blocks (age class >= 40): 675174
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.31 MB
- Schedules: 0.80 MB
- Runs: 0.00 MB
- Total: 28.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
