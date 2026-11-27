# WS4 tiled 30-m dataset — M2|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M2|BC|S13` (parent `M2|BC`)
- Tile / row / col: `M2` / 1 / 3
- Province: `BC`
- Centroid: 56.550903, -131.306617
- Allocated harvest: 3215.552870 m3
- Productive subcell area: 6362.601340 ha
- Committed geometry area: 30157.095111 ha
- Clipped inventory geometry: 30157.095111 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 94366
- Blocks: 52400
- Forest area: 8492.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4580
- Scheduled area: 670.05 ha
- Eligible blocks (age class >= 40): 45799
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.84 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 1.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
