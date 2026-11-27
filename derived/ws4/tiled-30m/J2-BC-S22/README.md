# WS4 tiled 30-m dataset — J2|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J2|BC|S22` (parent `J2|BC`)
- Tile / row / col: `J2` / 2 / 2
- Province: `BC`
- Centroid: 52.997795, -128.807767
- Allocated harvest: 118494.327543 m3
- Productive subcell area: 156198.926142 ha
- Committed geometry area: 213927.479276 ha
- Clipped inventory geometry: 213927.479276 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2104321
- Blocks: 1089900
- Forest area: 189388.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 106979
- Scheduled area: 18606.60 ha
- Eligible blocks (age class >= 40): 1069790
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.60 MB
- Schedules: 1.28 MB
- Runs: 0.00 MB
- Total: 30.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
