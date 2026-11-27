# WS4 tiled 30-m dataset — D29|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D29|QC|S32` (parent `D29|QC`)
- Tile / row / col: `D29` / 3 / 2
- Province: `QC`
- Centroid: 47.206359, -69.531705
- Allocated harvest: 10943.220269 m3
- Productive subcell area: 19092.525107 ha
- Committed geometry area: 20657.399143 ha
- Clipped inventory geometry: 20657.399143 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 219784
- Blocks: 65571
- Forest area: 19780.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5863
- Scheduled area: 1844.19 ha
- Eligible blocks (age class >= 40): 58623
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.98 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
