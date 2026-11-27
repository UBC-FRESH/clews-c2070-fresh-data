# WS4 tiled 30-m dataset — P10|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P10|NT|S33` (parent `P10|NT`)
- Tile / row / col: `P10` / 3 / 3
- Province: `NT`
- Centroid: 65.796376, -115.302898
- Allocated harvest: 46.443152 m3
- Productive subcell area: 94609.732188 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 846455
- Blocks: 470769
- Forest area: 76180.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30282
- Scheduled area: 5170.59 ha
- Eligible blocks (age class >= 40): 302818
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.72 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 13.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
