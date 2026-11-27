# WS4 tiled 30-m dataset — H36|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H36|NL|S31` (parent `H36|NL`)
- Tile / row / col: `H36` / 3 / 1
- Province: `NL`
- Centroid: 47.171360, -53.886432
- Allocated harvest: 5169.410477 m3
- Productive subcell area: 64654.694825 ha
- Committed geometry area: 120432.511374 ha
- Clipped inventory geometry: 120432.511374 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 787872
- Blocks: 362888
- Forest area: 70908.48 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31533
- Scheduled area: 6183.63 ha
- Eligible blocks (age class >= 40): 315328
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.95 MB
- Schedules: 0.37 MB
- Runs: 0.00 MB
- Total: 11.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
