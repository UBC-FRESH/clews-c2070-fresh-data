# WS4 tiled 30-m dataset — J29|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J29|NL|S33` (parent `J29|NL`)
- Tile / row / col: `J29` / 3 / 3
- Province: `NL`
- Centroid: 54.172407, -63.087056
- Allocated harvest: 6509.486467 m3
- Productive subcell area: 139235.398303 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1384552
- Blocks: 614569
- Forest area: 124609.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55680
- Scheduled area: 11259.45 ha
- Eligible blocks (age class >= 40): 556793
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.56 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 19.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
