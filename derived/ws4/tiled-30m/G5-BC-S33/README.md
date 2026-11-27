# WS4 tiled 30-m dataset — G5|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G5|BC|S33` (parent `G5|BC`)
- Tile / row / col: `G5` / 3 / 3
- Province: `BC`
- Centroid: 51.749500, -119.524306
- Allocated harvest: 139454.892072 m3
- Productive subcell area: 210408.981546 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2591241
- Blocks: 1095341
- Forest area: 233211.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 102410
- Scheduled area: 18142.02 ha
- Eligible blocks (age class >= 40): 1024100
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 33.29 MB
- Schedules: 1.23 MB
- Runs: 0.00 MB
- Total: 34.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
