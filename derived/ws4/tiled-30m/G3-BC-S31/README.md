# WS4 tiled 30-m dataset — G3|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G3|BC|S31` (parent `G3|BC`)
- Tile / row / col: `G3` / 3 / 1
- Province: `BC`
- Centroid: 50.419388, -124.752365
- Allocated harvest: 114051.176453 m3
- Productive subcell area: 130722.391880 ha
- Committed geometry area: 183968.249962 ha
- Clipped inventory geometry: 183968.249962 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1732756
- Blocks: 928569
- Forest area: 155948.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 88671
- Scheduled area: 13311.18 ha
- Eligible blocks (age class >= 40): 886702
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.01 MB
- Schedules: 1.05 MB
- Runs: 0.00 MB
- Total: 26.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
