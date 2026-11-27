# WS4 tiled 30-m dataset — E31|NB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E31|NB|S23` (parent `E31|NB`)
- Tile / row / col: `E31` / 2 / 3
- Province: `NB`
- Centroid: 46.472754, -64.807771
- Allocated harvest: 78675.011618 m3
- Productive subcell area: 98251.448598 ha
- Committed geometry area: 108398.324881 ha
- Clipped inventory geometry: 108398.324881 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 950430
- Blocks: 350172
- Forest area: 85538.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27547
- Scheduled area: 5751.90 ha
- Eligible blocks (age class >= 40): 275469
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.88 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 12.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
