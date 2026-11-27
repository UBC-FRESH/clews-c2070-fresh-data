# WS4 tiled 30-m dataset — G2|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G2|BC|S12` (parent `G2|BC`)
- Tile / row / col: `G2` / 1 / 2
- Province: `BC`
- Centroid: 49.102755, -125.340551
- Allocated harvest: 150637.051900 m3
- Productive subcell area: 148216.539125 ha
- Committed geometry area: 163117.710729 ha
- Clipped inventory geometry: 163117.710729 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1645932
- Blocks: 708611
- Forest area: 148133.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69363
- Scheduled area: 13231.71 ha
- Eligible blocks (age class >= 40): 693624
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.21 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 22.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
