# WS4 tiled 30-m dataset — H10|SK|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H10|SK|S11` (parent `H10|SK`)
- Tile / row / col: `H10` / 1 / 1
- Province: `SK`
- Centroid: 53.873282, -109.996317
- Allocated harvest: 166.565856 m3
- Productive subcell area: 647.810116 ha
- Committed geometry area: 869.226040 ha
- Clipped inventory geometry: 869.226040 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 7797
- Blocks: 3146
- Forest area: 701.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2886
- Scheduled area: 647.82 ha
- Eligible blocks (age class >= 40): 2886
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.19 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
