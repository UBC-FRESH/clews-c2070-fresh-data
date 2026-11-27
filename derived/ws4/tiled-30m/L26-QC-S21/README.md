# WS4 tiled 30-m dataset — L26|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L26|QC|S21` (parent `L26|QC`)
- Tile / row / col: `L26` / 2 / 1
- Province: `QC`
- Centroid: 58.442082, -69.456375
- Allocated harvest: 15956.319476 m3
- Productive subcell area: 91336.956437 ha
- Committed geometry area: 245582.614779 ha
- Clipped inventory geometry: 245582.614779 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 178603
- Blocks: 111186
- Forest area: 16074.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6342
- Scheduled area: 799.20 ha
- Eligible blocks (age class >= 40): 63413
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.54 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 3.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
