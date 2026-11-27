# WS4 tiled 30-m dataset — L2|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L2|BC|S13` (parent `L2|BC`)
- Tile / row / col: `L2` / 1 / 3
- Province: `BC`
- Centroid: 55.156014, -129.951228
- Allocated harvest: 42609.182868 m3
- Productive subcell area: 51824.398034 ha
- Committed geometry area: 86686.802099 ha
- Clipped inventory geometry: 86686.802099 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 770814
- Blocks: 420532
- Forest area: 69373.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41010
- Scheduled area: 6742.08 ha
- Eligible blocks (age class >= 40): 410099
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.52 MB
- Schedules: 0.48 MB
- Runs: 0.00 MB
- Total: 12.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
