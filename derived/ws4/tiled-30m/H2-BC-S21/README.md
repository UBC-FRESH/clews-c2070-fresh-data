# WS4 tiled 30-m dataset — H2|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H2|BC|S21` (parent `H2|BC`)
- Tile / row / col: `H2` / 2 / 1
- Province: `BC`
- Centroid: 50.398462, -127.274760
- Allocated harvest: 166224.635335 m3
- Productive subcell area: 189451.439836 ha
- Committed geometry area: 228284.351696 ha
- Clipped inventory geometry: 228284.351696 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2381653
- Blocks: 827740
- Forest area: 214348.77 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 80851
- Scheduled area: 15953.31 ha
- Eligible blocks (age class >= 40): 808507
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.56 MB
- Schedules: 0.96 MB
- Runs: 0.00 MB
- Total: 28.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
