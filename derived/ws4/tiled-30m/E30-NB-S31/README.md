# WS4 tiled 30-m dataset — E30|NB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E30|NB|S31` (parent `E30|NB`)
- Tile / row / col: `E30` / 3 / 1
- Province: `NB`
- Centroid: 47.801592, -67.328531
- Allocated harvest: 125871.500843 m3
- Productive subcell area: 119082.859696 ha
- Committed geometry area: 125539.975070 ha
- Clipped inventory geometry: 125539.975070 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1337866
- Blocks: 423042
- Forest area: 120407.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32962
- Scheduled area: 7735.95 ha
- Eligible blocks (age class >= 40): 329615
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.04 MB
- Schedules: 0.39 MB
- Runs: 0.00 MB
- Total: 16.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
