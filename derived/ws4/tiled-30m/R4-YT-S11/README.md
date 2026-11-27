# WS4 tiled 30-m dataset — R4|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R4|YT|S11` (parent `R4|YT`)
- Tile / row / col: `R4` / 1 / 1
- Province: `YT`
- Centroid: 63.086526, -136.347287
- Allocated harvest: 337.589146 m3
- Productive subcell area: 176424.897866 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2146183
- Blocks: 567012
- Forest area: 193156.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45673
- Scheduled area: 12998.25 ha
- Eligible blocks (age class >= 40): 456724
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.84 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 23.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
