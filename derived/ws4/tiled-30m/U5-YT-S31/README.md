# WS4 tiled 30-m dataset — U5|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U5|YT|S31` (parent `U5|YT`)
- Tile / row / col: `U5` / 3 / 1
- Province: `YT`
- Centroid: 67.882954, -140.915492
- Allocated harvest: 8.274247 m3
- Productive subcell area: 4791.434225 ha
- Committed geometry area: 14649.415448 ha
- Clipped inventory geometry: 14649.415448 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 66394
- Blocks: 31218
- Forest area: 5975.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1762
- Scheduled area: 295.11 ha
- Eligible blocks (age class >= 40): 17616
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.21 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
