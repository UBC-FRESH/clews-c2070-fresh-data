# WS4 tiled 30-m dataset — J10|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J10|SK|S13` (parent `J10|SK`)
- Tile / row / col: `J10` / 1 / 3
- Province: `SK`
- Centroid: 56.914596, -109.803722
- Allocated harvest: 12877.203924 m3
- Productive subcell area: 96800.171115 ha
- Committed geometry area: 117555.415969 ha
- Clipped inventory geometry: 117555.415969 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1082600
- Blocks: 171826
- Forest area: 97434.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9483
- Scheduled area: 2138.94 ha
- Eligible blocks (age class >= 40): 94825
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.31 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 9.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
