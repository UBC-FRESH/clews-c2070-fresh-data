# WS4 tiled 30-m dataset — E24|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E24|ON|S21` (parent `E24|ON`)
- Tile / row / col: `E24` / 2 / 1
- Province: `ON`
- Centroid: 50.099886, -79.540124
- Allocated harvest: 452.057783 m3
- Productive subcell area: 4207.274880 ha
- Committed geometry area: 4936.346070 ha
- Clipped inventory geometry: 4936.346070 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 51728
- Blocks: 20773
- Forest area: 4655.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1974
- Scheduled area: 436.86 ha
- Eligible blocks (age class >= 40): 19731
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.89 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
