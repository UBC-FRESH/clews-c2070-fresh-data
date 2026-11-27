# WS4 tiled 30-m dataset — L7|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|BC|S11` (parent `L7|BC`)
- Tile / row / col: `L7` / 1 / 1
- Province: `BC`
- Centroid: 57.943823, -120.548787
- Allocated harvest: 87517.106624 m3
- Productive subcell area: 214010.382010 ha
- Committed geometry area: 249859.707992 ha
- Clipped inventory geometry: 249859.707992 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2671392
- Blocks: 937895
- Forest area: 240425.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 87563
- Scheduled area: 21580.02 ha
- Eligible blocks (age class >= 40): 875622
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 32.05 MB
- Schedules: 1.04 MB
- Runs: 0.00 MB
- Total: 33.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
