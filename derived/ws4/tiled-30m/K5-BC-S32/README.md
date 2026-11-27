# WS4 tiled 30-m dataset — K5|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K5|BC|S32` (parent `K5|BC`)
- Tile / row / col: `K5` / 3 / 2
- Province: `BC`
- Centroid: 56.568057, -124.053953
- Allocated harvest: 78071.016193 m3
- Productive subcell area: 201267.521455 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2240060
- Blocks: 993766
- Forest area: 201605.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 94789
- Scheduled area: 17448.66 ha
- Eligible blocks (age class >= 40): 947889
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.98 MB
- Schedules: 1.13 MB
- Runs: 0.00 MB
- Total: 31.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
