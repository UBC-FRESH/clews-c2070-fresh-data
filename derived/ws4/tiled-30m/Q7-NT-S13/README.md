# WS4 tiled 30-m dataset — Q7|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q7|NT|S13` (parent `Q7|NT`)
- Tile / row / col: `Q7` / 1 / 3
- Province: `NT`
- Centroid: 64.619943, -124.888974
- Allocated harvest: 140.807692 m3
- Productive subcell area: 144411.735102 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1964608
- Blocks: 675877
- Forest area: 176814.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51684
- Scheduled area: 11664.00 ha
- Eligible blocks (age class >= 40): 516837
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.83 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 23.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
