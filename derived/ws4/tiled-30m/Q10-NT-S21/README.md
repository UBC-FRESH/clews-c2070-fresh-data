# WS4 tiled 30-m dataset — Q10|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q10|NT|S21` (parent `Q10|NT`)
- Tile / row / col: `Q10` / 2 / 1
- Province: `NT`
- Centroid: 66.357391, -118.212674
- Allocated harvest: 35.330298 m3
- Productive subcell area: 82136.501364 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 346138
- Blocks: 197222
- Forest area: 31152.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12231
- Scheduled area: 1840.14 ha
- Eligible blocks (age class >= 40): 122310
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.86 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 6.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
