# WS4 tiled 30-m dataset — E24|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E24|QC|S21` (parent `E24|QC`)
- Tile / row / col: `E24` / 2 / 1
- Province: `QC`
- Centroid: 50.211518, -79.151344
- Allocated harvest: 34781.824963 m3
- Productive subcell area: 170571.235962 ha
- Committed geometry area: 245063.653930 ha
- Clipped inventory geometry: 245063.653930 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2005932
- Blocks: 744553
- Forest area: 180533.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65971
- Scheduled area: 15415.92 ha
- Eligible blocks (age class >= 40): 659704
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.67 MB
- Schedules: 0.78 MB
- Runs: 0.00 MB
- Total: 25.45 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
