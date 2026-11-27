# WS4 tiled 30-m dataset — B28|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B28|QC|S31` (parent `B28|QC`)
- Tile / row / col: `B28` / 3 / 1
- Province: `QC`
- Centroid: 45.231534, -73.105355
- Allocated harvest: 73734.421900 m3
- Productive subcell area: 118315.077580 ha
- Committed geometry area: 228363.429864 ha
- Clipped inventory geometry: 228363.429864 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 983065
- Blocks: 300544
- Forest area: 88475.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18580
- Scheduled area: 5076.00 ha
- Eligible blocks (age class >= 40): 185793
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.46 MB
- Schedules: 0.22 MB
- Runs: 0.00 MB
- Total: 11.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
