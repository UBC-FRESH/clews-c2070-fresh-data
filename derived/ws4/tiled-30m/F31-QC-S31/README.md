# WS4 tiled 30-m dataset — F31|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F31|QC|S31` (parent `F31|QC`)
- Tile / row / col: `F31` / 3 / 1
- Province: `QC`
- Centroid: 48.550845, -64.648227
- Allocated harvest: 97562.481380 m3
- Productive subcell area: 195592.460065 ha
- Committed geometry area: 208407.181892 ha
- Clipped inventory geometry: 208407.181892 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2190273
- Blocks: 818371
- Forest area: 197124.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76049
- Scheduled area: 17734.05 ha
- Eligible blocks (age class >= 40): 760482
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.20 MB
- Schedules: 0.90 MB
- Runs: 0.00 MB
- Total: 28.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
