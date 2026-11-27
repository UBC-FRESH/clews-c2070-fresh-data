# WS4 tiled 30-m dataset — E31|NB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E31|NB|S32` (parent `E31|NB`)
- Tile / row / col: `E31` / 3 / 2
- Province: `NB`
- Centroid: 46.993005, -64.925747
- Allocated harvest: 68791.192010 m3
- Productive subcell area: 85908.271595 ha
- Committed geometry area: 94780.411558 ha
- Clipped inventory geometry: 94780.411558 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 803362
- Blocks: 323321
- Forest area: 72302.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27015
- Scheduled area: 5731.11 ha
- Eligible blocks (age class >= 40): 270146
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.60 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 10.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
