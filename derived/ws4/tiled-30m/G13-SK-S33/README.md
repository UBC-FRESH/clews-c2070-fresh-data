# WS4 tiled 30-m dataset — G13|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G13|SK|S33` (parent `G13|SK`)
- Tile / row / col: `G13` / 3 / 3
- Province: `SK`
- Centroid: 54.435935, -102.037282
- Allocated harvest: 21077.208819 m3
- Productive subcell area: 93828.535590 ha
- Committed geometry area: 131717.834745 ha
- Clipped inventory geometry: 131717.834745 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 794225
- Blocks: 299507
- Forest area: 71480.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28501
- Scheduled area: 6539.31 ha
- Eligible blocks (age class >= 40): 285010
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.34 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 10.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
