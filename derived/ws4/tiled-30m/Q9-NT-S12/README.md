# WS4 tiled 30-m dataset — Q9|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q9|NT|S12` (parent `Q9|NT`)
- Tile / row / col: `Q9` / 1 / 2
- Province: `NT`
- Centroid: 65.586240, -119.901887
- Allocated harvest: 45.367961 m3
- Productive subcell area: 76940.164223 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 829689
- Blocks: 384716
- Forest area: 74672.01 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36175
- Scheduled area: 6519.60 ha
- Eligible blocks (age class >= 40): 361749
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.56 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 11.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
