# WS4 tiled 30-m dataset — D19|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D19|ON|S11` (parent `D19|ON`)
- Tile / row / col: `D19` / 1 / 1
- Province: `ON`
- Centroid: 49.532854, -89.954786
- Allocated harvest: 48562.975834 m3
- Productive subcell area: 185647.724250 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2327555
- Blocks: 663207
- Forest area: 209479.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57043
- Scheduled area: 14946.57 ha
- Eligible blocks (age class >= 40): 570426
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.10 MB
- Schedules: 0.67 MB
- Runs: 0.00 MB
- Total: 26.77 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
