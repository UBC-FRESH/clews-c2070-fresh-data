# WS4 tiled 30-m dataset — F3|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F3|BC|S31` (parent `F3|BC`)
- Tile / row / col: `F3` / 3 / 1
- Province: `BC`
- Centroid: 48.996021, -123.930075
- Allocated harvest: 103077.073468 m3
- Productive subcell area: 102672.444818 ha
- Committed geometry area: 152079.895600 ha
- Clipped inventory geometry: 152079.895600 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1438386
- Blocks: 499942
- Forest area: 129454.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44575
- Scheduled area: 8710.11 ha
- Eligible blocks (age class >= 40): 445744
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.58 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 18.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
