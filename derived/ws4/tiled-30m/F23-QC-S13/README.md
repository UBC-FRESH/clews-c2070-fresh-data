# WS4 tiled 30-m dataset — F23|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F23|QC|S13` (parent `F23|QC`)
- Tile / row / col: `F23` / 1 / 3
- Province: `QC`
- Centroid: 51.188272, -79.331744
- Allocated harvest: 10979.242184 m3
- Productive subcell area: 86395.576260 ha
- Committed geometry area: 130505.611726 ha
- Clipped inventory geometry: 130505.611726 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 917781
- Blocks: 308458
- Forest area: 82600.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27449
- Scheduled area: 7380.45 ha
- Eligible blocks (age class >= 40): 274484
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.21 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 11.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
