# WS4 tiled 30-m dataset — T4|YT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T4|YT|S22` (parent `T4|YT`)
- Tile / row / col: `T4` / 2 / 2
- Province: `YT`
- Centroid: 65.895384, -140.239679
- Allocated harvest: 168.687651 m3
- Productive subcell area: 133190.778382 ha
- Committed geometry area: 249797.772073 ha
- Clipped inventory geometry: 249797.772073 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1393631
- Blocks: 649561
- Forest area: 125426.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47075
- Scheduled area: 8643.51 ha
- Eligible blocks (age class >= 40): 470747
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.20 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 19.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
