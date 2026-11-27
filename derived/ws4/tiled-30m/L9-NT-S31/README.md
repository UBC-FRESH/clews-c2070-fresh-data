# WS4 tiled 30-m dataset — L9|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L9|NT|S31` (parent `L9|NT`)
- Tile / row / col: `L9` / 3 / 1
- Province: `NT`
- Centroid: 60.031187, -116.074592
- Allocated harvest: 15.595085 m3
- Productive subcell area: 10266.297852 ha
- Committed geometry area: 16251.046627 ha
- Clipped inventory geometry: 16251.046627 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 119501
- Blocks: 25790
- Forest area: 10755.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2067
- Scheduled area: 503.73 ha
- Eligible blocks (age class >= 40): 20670
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.46 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.48 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
