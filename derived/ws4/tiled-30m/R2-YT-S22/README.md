# WS4 tiled 30-m dataset — R2|YT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R2|YT|S22` (parent `R2|YT`)
- Tile / row / col: `R2` / 2 / 2
- Province: `YT`
- Centroid: 61.980249, -140.706700
- Allocated harvest: 185.481251 m3
- Productive subcell area: 87995.180462 ha
- Committed geometry area: 170745.626374 ha
- Clipped inventory geometry: 170745.626374 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1122658
- Blocks: 513711
- Forest area: 101039.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42179
- Scheduled area: 7921.89 ha
- Eligible blocks (age class >= 40): 421790
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.47 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 15.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
