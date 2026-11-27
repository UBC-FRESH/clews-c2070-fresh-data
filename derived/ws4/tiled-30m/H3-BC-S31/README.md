# WS4 tiled 30-m dataset — H3|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H3|BC|S31` (parent `H3|BC`)
- Tile / row / col: `H3` / 3 / 1
- Province: `BC`
- Centroid: 51.456445, -125.732639
- Allocated harvest: 91768.239037 m3
- Productive subcell area: 139257.618241 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 785048
- Blocks: 453786
- Forest area: 70654.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41414
- Scheduled area: 6068.16 ha
- Eligible blocks (age class >= 40): 414133
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.07 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 12.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
