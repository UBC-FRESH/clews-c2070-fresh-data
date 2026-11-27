# WS4 tiled 30-m dataset — F31|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F31|QC|S21` (parent `F31|QC`)
- Tile / row / col: `F31` / 2 / 1
- Province: `QC`
- Centroid: 48.220741, -65.051283
- Allocated harvest: 47246.761118 m3
- Productive subcell area: 94719.918011 ha
- Committed geometry area: 100925.726764 ha
- Clipped inventory geometry: 100925.726764 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1023505
- Blocks: 350997
- Forest area: 92115.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32328
- Scheduled area: 8399.34 ha
- Eligible blocks (age class >= 40): 323271
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.53 MB
- Schedules: 0.38 MB
- Runs: 0.00 MB
- Total: 12.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
