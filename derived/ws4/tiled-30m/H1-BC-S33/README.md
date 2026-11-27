# WS4 tiled 30-m dataset — H1|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H1|BC|S33` (parent `H1|BC`)
- Tile / row / col: `H1` / 3 / 3
- Province: `BC`
- Centroid: 50.651038, -128.099855
- Allocated harvest: 106280.061654 m3
- Productive subcell area: 99639.738403 ha
- Committed geometry area: 104310.793632 ha
- Clipped inventory geometry: 104310.793632 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1107762
- Blocks: 435233
- Forest area: 99698.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42554
- Scheduled area: 7118.19 ha
- Eligible blocks (age class >= 40): 425533
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.72 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 14.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
