# WS4 tiled 30-m dataset — F34|NS|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F34|NS|S11` (parent `F34|NS`)
- Tile / row / col: `F34` / 1 / 1
- Province: `NS`
- Centroid: 45.858153, -60.258943
- Allocated harvest: 24142.558990 m3
- Productive subcell area: 83984.813931 ha
- Committed geometry area: 104310.079384 ha
- Clipped inventory geometry: 104310.079384 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 934616
- Blocks: 342834
- Forest area: 84115.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29451
- Scheduled area: 6475.14 ha
- Eligible blocks (age class >= 40): 294503
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.68 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 12.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
