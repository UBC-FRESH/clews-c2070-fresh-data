# WS4 tiled 30-m dataset — L7|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|BC|S31` (parent `L7|BC`)
- Tile / row / col: `L7` / 3 / 1
- Province: `BC`
- Centroid: 58.789939, -121.242900
- Allocated harvest: 87566.246002 m3
- Productive subcell area: 214130.545227 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1783782
- Blocks: 583026
- Forest area: 160540.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36169
- Scheduled area: 5410.62 ha
- Eligible blocks (age class >= 40): 361685
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.20 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 20.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
