# WS4 tiled 30-m dataset — I17|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I17|MB|S22` (parent `I17|MB`)
- Tile / row / col: `I17` / 2 / 2
- Province: `MB`
- Centroid: 56.937079, -93.086693
- Allocated harvest: 1679.735724 m3
- Productive subcell area: 122118.053125 ha
- Committed geometry area: 245638.243528 ha
- Clipped inventory geometry: 245638.243528 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1196492
- Blocks: 574419
- Forest area: 107684.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47260
- Scheduled area: 8181.99 ha
- Eligible blocks (age class >= 40): 472598
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.53 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 17.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
