# WS4 tiled 30-m dataset — M10|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M10|NT|S33` (parent `M10|NT`)
- Tile / row / col: `M10` / 3 / 3
- Province: `NT`
- Centroid: 61.815233, -112.541298
- Allocated harvest: 165.218418 m3
- Productive subcell area: 123265.143318 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 963636
- Blocks: 354003
- Forest area: 86727.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28533
- Scheduled area: 6151.68 ha
- Eligible blocks (age class >= 40): 285330
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.78 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 12.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
