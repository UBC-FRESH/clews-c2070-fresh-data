# WS4 tiled 30-m dataset — L31|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L31|NL|S12` (parent `L31|NL`)
- Tile / row / col: `L31` / 1 / 2
- Province: `NL`
- Centroid: 54.572058, -58.131283
- Allocated harvest: 7259.332910 m3
- Productive subcell area: 122403.337232 ha
- Committed geometry area: 220238.954266 ha
- Clipped inventory geometry: 220238.954266 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1698713
- Blocks: 556567
- Forest area: 152884.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43442
- Scheduled area: 11553.66 ha
- Eligible blocks (age class >= 40): 434414
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.94 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 20.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
