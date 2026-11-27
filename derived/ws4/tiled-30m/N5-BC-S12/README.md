# WS4 tiled 30-m dataset — N5|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|BC|S12` (parent `N5|BC`)
- Tile / row / col: `N5` / 1 / 2
- Province: `BC`
- Centroid: 59.429492, -126.850928
- Allocated harvest: 71478.149458 m3
- Productive subcell area: 221524.303503 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2628073
- Blocks: 1174867
- Forest area: 236526.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 113338
- Scheduled area: 21439.62 ha
- Eligible blocks (age class >= 40): 1133372
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 35.32 MB
- Schedules: 1.37 MB
- Runs: 0.00 MB
- Total: 36.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
