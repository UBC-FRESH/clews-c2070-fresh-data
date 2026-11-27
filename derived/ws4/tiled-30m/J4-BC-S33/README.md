# WS4 tiled 30-m dataset — J4|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J4|BC|S33` (parent `J4|BC`)
- Tile / row / col: `J4` / 3 / 3
- Province: `BC`
- Centroid: 54.928286, -124.428940
- Allocated harvest: 113986.006079 m3
- Productive subcell area: 218265.682259 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2501097
- Blocks: 838718
- Forest area: 225098.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75295
- Scheduled area: 15315.84 ha
- Eligible blocks (age class >= 40): 752946
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.67 MB
- Schedules: 0.89 MB
- Runs: 0.00 MB
- Total: 30.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
