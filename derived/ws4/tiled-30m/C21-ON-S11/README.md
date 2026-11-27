# WS4 tiled 30-m dataset — C21|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C21|ON|S11` (parent `C21|ON`)
- Tile / row / col: `C21` / 1 / 1
- Province: `ON`
- Centroid: 48.024901, -85.854499
- Allocated harvest: 7032.318413 m3
- Productive subcell area: 24562.081669 ha
- Committed geometry area: 27314.933008 ha
- Clipped inventory geometry: 27314.933008 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 284774
- Blocks: 94260
- Forest area: 25629.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9282
- Scheduled area: 2479.59 ha
- Eligible blocks (age class >= 40): 92820
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.01 MB
- Schedules: 0.10 MB
- Runs: 0.00 MB
- Total: 4.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
