# WS4 tiled 30-m dataset — K5|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K5|BC|S21` (parent `K5|BC`)
- Tile / row / col: `K5` / 2 / 1
- Province: `BC`
- Centroid: 55.952981, -124.427161
- Allocated harvest: 78071.016193 m3
- Productive subcell area: 201267.521455 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2268663
- Blocks: 776842
- Forest area: 204179.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68902
- Scheduled area: 13193.46 ha
- Eligible blocks (age class >= 40): 689020
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.86 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 27.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
