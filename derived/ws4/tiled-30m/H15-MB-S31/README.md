# WS4 tiled 30-m dataset — H15|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H15|MB|S31` (parent `H15|MB`)
- Tile / row / col: `H15` / 3 / 1
- Province: `MB`
- Centroid: 55.968684, -98.862082
- Allocated harvest: 7584.915428 m3
- Productive subcell area: 194721.647177 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1885482
- Blocks: 544202
- Forest area: 169693.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48472
- Scheduled area: 11664.00 ha
- Eligible blocks (age class >= 40): 484717
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.88 MB
- Schedules: 0.57 MB
- Runs: 0.00 MB
- Total: 21.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
