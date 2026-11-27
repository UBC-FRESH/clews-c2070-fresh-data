# WS4 tiled 30-m dataset — O9|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O9|NT|S31` (parent `O9|NT`)
- Tile / row / col: `O9` / 3 / 1
- Province: `NT`
- Centroid: 63.698024, -119.274179
- Allocated harvest: 90.559773 m3
- Productive subcell area: 115433.428079 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1975627
- Blocks: 766383
- Forest area: 177806.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66537
- Scheduled area: 15952.50 ha
- Eligible blocks (age class >= 40): 665361
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.50 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 25.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
