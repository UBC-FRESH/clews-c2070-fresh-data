# WS4 tiled 30-m dataset — M5|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M5|BC|S31` (parent `M5|BC`)
- Tile / row / col: `M5` / 3 / 1
- Province: `BC`
- Centroid: 58.802960, -127.203766
- Allocated harvest: 44439.105201 m3
- Productive subcell area: 135935.973745 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2032324
- Blocks: 934480
- Forest area: 182909.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 86622
- Scheduled area: 16046.10 ha
- Eligible blocks (age class >= 40): 866218
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.41 MB
- Schedules: 1.03 MB
- Runs: 0.00 MB
- Total: 28.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
