# WS4 tiled 30-m dataset — K29|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K29|QC|S31` (parent `K29|QC`)
- Tile / row / col: `K29` / 3 / 1
- Province: `QC`
- Centroid: 55.768422, -63.766690
- Allocated harvest: 1257.052420 m3
- Productive subcell area: 7634.811000 ha
- Committed geometry area: 15778.367734 ha
- Clipped inventory geometry: 15778.367734 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 29510
- Blocks: 16269
- Forest area: 2655.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 923
- Scheduled area: 127.35 ha
- Eligible blocks (age class >= 40): 9224
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.60 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.60 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
