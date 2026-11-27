# WS4 tiled 30-m dataset — O5|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O5|YT|S31` (parent `O5|YT`)
- Tile / row / col: `O5` / 3 / 1
- Province: `YT`
- Centroid: 61.196059, -129.991535
- Allocated harvest: 258.538255 m3
- Productive subcell area: 172813.327718 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1560747
- Blocks: 717915
- Forest area: 140467.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57720
- Scheduled area: 10282.50 ha
- Eligible blocks (age class >= 40): 577195
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.23 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 21.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
