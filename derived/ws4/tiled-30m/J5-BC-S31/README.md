# WS4 tiled 30-m dataset — J5|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J5|BC|S31` (parent `J5|BC`)
- Tile / row / col: `J5` / 3 / 1
- Province: `BC`
- Centroid: 55.130335, -123.713712
- Allocated harvest: 137778.097846 m3
- Productive subcell area: 216479.315979 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2621870
- Blocks: 940641
- Forest area: 235968.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 86076
- Scheduled area: 15791.22 ha
- Eligible blocks (age class >= 40): 860753
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.70 MB
- Schedules: 1.02 MB
- Runs: 0.00 MB
- Total: 32.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
