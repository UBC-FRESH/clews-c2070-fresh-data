# WS4 tiled 30-m dataset — K2|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K2|BC|S13` (parent `K2|BC`)
- Tile / row / col: `K2` / 1 / 3
- Province: `BC`
- Centroid: 54.033978, -128.952074
- Allocated harvest: 115142.564389 m3
- Productive subcell area: 161483.017982 ha
- Committed geometry area: 229504.842410 ha
- Clipped inventory geometry: 229504.842410 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1513003
- Blocks: 820513
- Forest area: 136170.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77038
- Scheduled area: 12338.10 ha
- Eligible blocks (age class >= 40): 770374
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.91 MB
- Schedules: 0.91 MB
- Runs: 0.00 MB
- Total: 22.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
