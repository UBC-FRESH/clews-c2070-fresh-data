# WS4 tiled 30-m dataset — E21|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E21|ON|S31` (parent `E21|ON`)
- Tile / row / col: `E21` / 3 / 1
- Province: `ON`
- Centroid: 51.465698, -85.321352
- Allocated harvest: 18244.320301 m3
- Productive subcell area: 126931.838764 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1581485
- Blocks: 445611
- Forest area: 142333.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41981
- Scheduled area: 14838.03 ha
- Eligible blocks (age class >= 40): 419801
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.99 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 18.48 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
