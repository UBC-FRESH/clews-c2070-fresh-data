# WS4 tiled 30-m dataset — I12|SK|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I12|SK|S11` (parent `I12|SK`)
- Tile / row / col: `I12` / 1 / 1
- Province: `SK`
- Centroid: 55.934165, -106.270144
- Allocated harvest: 23038.876296 m3
- Productive subcell area: 186188.790831 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2001881
- Blocks: 402740
- Forest area: 180169.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26573
- Scheduled area: 4140.27 ha
- Eligible blocks (age class >= 40): 265723
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.78 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 19.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
