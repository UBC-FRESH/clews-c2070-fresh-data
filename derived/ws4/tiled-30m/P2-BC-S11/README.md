# WS4 tiled 30-m dataset — P2|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P2|BC|S11` (parent `P2|BC`)
- Tile / row / col: `P2` / 1 / 1
- Province: `BC`
- Centroid: 59.227780, -137.295305
- Allocated harvest: 6793.305908 m3
- Productive subcell area: 20988.477281 ha
- Committed geometry area: 177990.771171 ha
- Clipped inventory geometry: 177990.771171 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 79414
- Blocks: 39957
- Forest area: 7147.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3237
- Scheduled area: 545.22 ha
- Eligible blocks (age class >= 40): 32369
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.49 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
