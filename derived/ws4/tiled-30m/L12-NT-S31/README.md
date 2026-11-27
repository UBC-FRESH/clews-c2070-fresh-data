# WS4 tiled 30-m dataset — L12|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L12|NT|S31` (parent `L12|NT`)
- Tile / row / col: `L12` / 3 / 1
- Province: `NT`
- Centroid: 60.909201, -108.110251
- Allocated harvest: 60.433136 m3
- Productive subcell area: 134974.445460 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1731592
- Blocks: 404328
- Forest area: 155843.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22988
- Scheduled area: 7002.54 ha
- Eligible blocks (age class >= 40): 229879
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.39 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 17.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
