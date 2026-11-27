# WS4 tiled 30-m dataset — G23|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G23|QC|S32` (parent `G23|QC`)
- Tile / row / col: `G23` / 3 / 2
- Province: `QC`
- Centroid: 53.485502, -79.030919
- Allocated harvest: 2838.822569 m3
- Productive subcell area: 15610.760076 ha
- Committed geometry area: 25827.436174 ha
- Clipped inventory geometry: 25827.436174 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 208242
- Blocks: 77000
- Forest area: 18741.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6977
- Scheduled area: 1760.94 ha
- Eligible blocks (age class >= 40): 69767
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.13 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 3.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
