# WS4 tiled 30-m dataset — G21|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G21|ON|S13` (parent `G21|ON`)
- Tile / row / col: `G21` / 1 / 3
- Province: `ON`
- Centroid: 53.106973, -83.365281
- Allocated harvest: 7752.746737 m3
- Productive subcell area: 117612.074200 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1051274
- Blocks: 492420
- Forest area: 94614.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43881
- Scheduled area: 8448.12 ha
- Eligible blocks (age class >= 40): 438806
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.37 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 14.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
