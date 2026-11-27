# WS4 tiled 30-m dataset — E13|SK|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E13|SK|S11` (parent `E13|SK`)
- Tile / row / col: `E13` / 1 / 1
- Province: `SK`
- Centroid: 50.725970, -102.656516
- Allocated harvest: 7564.483900 m3
- Productive subcell area: 34376.961027 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 238091
- Blocks: 79452
- Forest area: 21428.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4097
- Scheduled area: 1596.06 ha
- Eligible blocks (age class >= 40): 40964
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.28 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 3.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
