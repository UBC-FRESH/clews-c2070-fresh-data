# WS4 tiled 30-m dataset — F31|NB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F31|NB|S12` (parent `F31|NB`)
- Tile / row / col: `F31` / 1 / 2
- Province: `NB`
- Centroid: 47.578228, -64.884349
- Allocated harvest: 32015.035634 m3
- Productive subcell area: 36083.293393 ha
- Committed geometry area: 43509.322354 ha
- Clipped inventory geometry: 43509.322354 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 304621
- Blocks: 137901
- Forest area: 27415.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10153
- Scheduled area: 2069.91 ha
- Eligible blocks (age class >= 40): 101522
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.90 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 5.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
