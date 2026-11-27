# WS4 tiled 30-m dataset — C17|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C17|ON|S12` (parent `C17|ON`)
- Tile / row / col: `C17` / 1 / 2
- Province: `ON`
- Centroid: 48.524100, -93.716941
- Allocated harvest: 276.330201 m3
- Productive subcell area: 1252.402675 ha
- Committed geometry area: 1624.387005 ha
- Clipped inventory geometry: 1624.387005 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 8943
- Blocks: 2968
- Forest area: 804.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2008
- Scheduled area: 596.07 ha
- Eligible blocks (age class >= 40): 2008
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.20 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
