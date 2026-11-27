# WS4 tiled 30-m dataset — J2|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J2|BC|S23` (parent `J2|BC`)
- Tile / row / col: `J2` / 2 / 3
- Province: `BC`
- Centroid: 53.225630, -128.171997
- Allocated harvest: 133664.536330 m3
- Productive subcell area: 176196.257416 ha
- Committed geometry area: 241315.495169 ha
- Clipped inventory geometry: 241315.495169 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1327771
- Blocks: 831549
- Forest area: 119499.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76704
- Scheduled area: 10832.76 ha
- Eligible blocks (age class >= 40): 767036
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.77 MB
- Schedules: 0.91 MB
- Runs: 0.00 MB
- Total: 21.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
