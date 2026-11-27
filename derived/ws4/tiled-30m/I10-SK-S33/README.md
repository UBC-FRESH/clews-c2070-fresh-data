# WS4 tiled 30-m dataset — I10|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I10|SK|S33` (parent `I10|SK`)
- Tile / row / col: `I10` / 3 / 3
- Province: `SK`
- Centroid: 56.461306, -109.710878
- Allocated harvest: 29016.138777 m3
- Productive subcell area: 149938.973644 ha
- Committed geometry area: 177715.121242 ha
- Clipped inventory geometry: 177715.121242 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1413920
- Blocks: 382195
- Forest area: 127252.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27921
- Scheduled area: 6427.17 ha
- Eligible blocks (age class >= 40): 279205
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.39 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 15.72 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
