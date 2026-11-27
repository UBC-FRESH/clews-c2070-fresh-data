# WS4 tiled 30-m dataset — F5|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F5|BC|S33` (parent `F5|BC`)
- Tile / row / col: `F5` / 3 / 3
- Province: `BC`
- Centroid: 50.487329, -118.724996
- Allocated harvest: 161914.105795 m3
- Productive subcell area: 203427.507706 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2401286
- Blocks: 949874
- Forest area: 216115.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 85700
- Scheduled area: 16631.91 ha
- Eligible blocks (age class >= 40): 856994
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.41 MB
- Schedules: 1.02 MB
- Runs: 0.00 MB
- Total: 31.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
