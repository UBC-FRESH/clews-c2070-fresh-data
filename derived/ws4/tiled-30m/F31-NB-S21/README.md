# WS4 tiled 30-m dataset — F31|NB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F31|NB|S21` (parent `F31|NB`)
- Tile / row / col: `F31` / 2 / 1
- Province: `NB`
- Centroid: 47.824797, -64.783779
- Allocated harvest: 28.851386 m3
- Productive subcell area: 32.517628 ha
- Committed geometry area: 39.209835 ha
- Clipped inventory geometry: 39.209835 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 74
- Blocks: 55
- Forest area: 6.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23
- Scheduled area: 2.88 ha
- Eligible blocks (age class >= 40): 23
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
