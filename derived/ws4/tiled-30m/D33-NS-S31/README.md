# WS4 tiled 30-m dataset — D33|NS|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D33|NS|S31` (parent `D33|NS`)
- Tile / row / col: `D33` / 3 / 1
- Province: `NS`
- Centroid: 44.924981, -63.024622
- Allocated harvest: 90436.468396 m3
- Productive subcell area: 187765.502046 ha
- Committed geometry area: 227330.587202 ha
- Clipped inventory geometry: 227330.587202 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2176172
- Blocks: 632526
- Forest area: 195855.48 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52348
- Scheduled area: 13007.34 ha
- Eligible blocks (age class >= 40): 523474
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.26 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 24.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
