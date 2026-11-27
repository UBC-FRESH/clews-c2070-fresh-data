# WS4 tiled 30-m dataset — L7|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|BC|S32` (parent `L7|BC`)
- Tile / row / col: `L7` / 3 / 2
- Province: `BC`
- Centroid: 58.975304, -120.447145
- Allocated harvest: 83658.117406 m3
- Productive subcell area: 204573.783972 ha
- Committed geometry area: 238842.365711 ha
- Clipped inventory geometry: 238842.365711 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1822860
- Blocks: 718910
- Forest area: 164057.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52857
- Scheduled area: 8314.56 ha
- Eligible blocks (age class >= 40): 528569
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.44 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 23.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
