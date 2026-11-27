# WS4 tiled 30-m dataset — D28|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D28|QC|S23` (parent `D28|QC`)
- Tile / row / col: `D28` / 2 / 3
- Province: `QC`
- Centroid: 46.930774, -70.566632
- Allocated harvest: 84637.755304 m3
- Productive subcell area: 144330.227477 ha
- Committed geometry area: 182191.185370 ha
- Clipped inventory geometry: 182191.185370 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1338022
- Blocks: 451263
- Forest area: 120421.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38052
- Scheduled area: 9933.57 ha
- Eligible blocks (age class >= 40): 380515
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.42 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 16.87 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
