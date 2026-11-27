# WS4 tiled 30-m dataset — I12|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I12|SK|S13` (parent `I12|SK`)
- Tile / row / col: `I12` / 1 / 3
- Province: `SK`
- Centroid: 56.084435, -104.654253
- Allocated harvest: 23038.876296 m3
- Productive subcell area: 186188.790831 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2019625
- Blocks: 297471
- Forest area: 181766.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13537
- Scheduled area: 3293.19 ha
- Eligible blocks (age class >= 40): 135366
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.23 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 17.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
