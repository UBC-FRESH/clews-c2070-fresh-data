# WS4 tiled 30-m dataset — K7|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K7|BC|S31` (parent `K7|BC`)
- Tile / row / col: `K7` / 3 / 1
- Province: `BC`
- Centroid: 57.519928, -120.311890
- Allocated harvest: 73296.418653 m3
- Productive subcell area: 182988.681531 ha
- Committed geometry area: 192777.613754 ha
- Clipped inventory geometry: 192777.613754 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1986077
- Blocks: 783419
- Forest area: 178746.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 71077
- Scheduled area: 13596.12 ha
- Eligible blocks (age class >= 40): 710770
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.68 MB
- Schedules: 0.84 MB
- Runs: 0.00 MB
- Total: 25.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
