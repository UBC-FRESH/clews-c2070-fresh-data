# WS4 tiled 30-m dataset — K29|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K29|NL|S22` (parent `K29|NL`)
- Tile / row / col: `K29` / 2 / 2
- Province: `NL`
- Centroid: 55.194463, -63.017744
- Allocated harvest: 5618.782411 m3
- Productive subcell area: 117412.131892 ha
- Committed geometry area: 249305.569922 ha
- Clipped inventory geometry: 249305.569922 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 705061
- Blocks: 436192
- Forest area: 63455.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32390
- Scheduled area: 4197.60 ha
- Eligible blocks (age class >= 40): 323896
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.14 MB
- Schedules: 0.38 MB
- Runs: 0.00 MB
- Total: 11.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
