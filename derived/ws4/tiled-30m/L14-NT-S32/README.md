# WS4 tiled 30-m dataset — L14|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L14|NT|S32` (parent `L14|NT`)
- Tile / row / col: `L14` / 3 / 2
- Province: `NT`
- Centroid: 61.579454, -102.007577
- Allocated harvest: 0.077594 m3
- Productive subcell area: 199.631803 ha
- Committed geometry area: 628.878606 ha
- Clipped inventory geometry: 628.878606 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 124
- Blocks: 112
- Forest area: 11.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28
- Scheduled area: 2.61 ha
- Eligible blocks (age class >= 40): 28
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
