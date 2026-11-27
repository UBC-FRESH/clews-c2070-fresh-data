# WS4 tiled 30-m dataset — E30|NB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E30|NB|S22` (parent `E30|NB`)
- Tile / row / col: `E30` / 2 / 2
- Province: `NB`
- Centroid: 47.312342, -66.991639
- Allocated harvest: 250660.199616 m3
- Productive subcell area: 237141.316202 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2655228
- Blocks: 844878
- Forest area: 238970.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66248
- Scheduled area: 14805.00 ha
- Eligible blocks (age class >= 40): 662478
- Simulated years: 20
- Harvested volume: 2947643.776 m3
- Treated/managed area: 14805.000 ha

## Storage

- Dataset: 30.95 MB
- Schedules: 0.79 MB
- Runs: 16.20 MB
- Total: 47.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
