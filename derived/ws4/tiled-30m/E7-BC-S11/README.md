# WS4 tiled 30-m dataset — E7|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E7|BC|S11` (parent `E7|BC`)
- Tile / row / col: `E7` / 1 / 1
- Province: `BC`
- Centroid: 49.097007, -114.952152
- Allocated harvest: 68509.439562 m3
- Productive subcell area: 80696.454808 ha
- Committed geometry area: 107751.777226 ha
- Clipped inventory geometry: 107751.777226 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 939904
- Blocks: 462969
- Forest area: 84591.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42585
- Scheduled area: 7268.85 ha
- Eligible blocks (age class >= 40): 425848
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.31 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 13.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
