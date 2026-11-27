# WS4 tiled 30-m dataset — G14|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G14|MB|S13` (parent `G14|MB`)
- Tile / row / col: `G14` / 1 / 3
- Province: `MB`
- Centroid: 53.655894, -99.395735
- Allocated harvest: 5805.608277 m3
- Productive subcell area: 146461.461203 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1971326
- Blocks: 568949
- Forest area: 177419.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48595
- Scheduled area: 13483.71 ha
- Eligible blocks (age class >= 40): 485949
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.80 MB
- Schedules: 0.57 MB
- Runs: 0.00 MB
- Total: 22.37 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
