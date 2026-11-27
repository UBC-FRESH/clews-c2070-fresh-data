# WS4 tiled 30-m dataset — H31|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H31|QC|S23` (parent `H31|QC`)
- Tile / row / col: `H31` / 2 / 3
- Province: `QC`
- Centroid: 50.224624, -61.724470
- Allocated harvest: 13546.034077 m3
- Productive subcell area: 44013.706622 ha
- Committed geometry area: 61292.738815 ha
- Clipped inventory geometry: 61292.738815 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 213245
- Blocks: 119813
- Forest area: 19192.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9986
- Scheduled area: 1692.27 ha
- Eligible blocks (age class >= 40): 99859
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.02 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 4.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
