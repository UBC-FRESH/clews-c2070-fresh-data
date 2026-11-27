# WS4 tiled 30-m dataset — L7|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|BC|S21` (parent `L7|BC`)
- Tile / row / col: `L7` / 2 / 1
- Province: `BC`
- Centroid: 58.367214, -120.891291
- Allocated harvest: 87566.246002 m3
- Productive subcell area: 214130.545227 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2178545
- Blocks: 822213
- Forest area: 196069.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66619
- Scheduled area: 11146.05 ha
- Eligible blocks (age class >= 40): 666181
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.30 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 27.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
