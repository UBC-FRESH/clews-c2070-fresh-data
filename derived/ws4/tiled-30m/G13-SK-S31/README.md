# WS4 tiled 30-m dataset — G13|SK|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G13|SK|S31` (parent `G13|SK`)
- Tile / row / col: `G13` / 3 / 1
- Province: `SK`
- Centroid: 54.335549, -103.407939
- Allocated harvest: 40004.470274 m3
- Productive subcell area: 178086.239749 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2497497
- Blocks: 1018370
- Forest area: 224774.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 100014
- Scheduled area: 21523.68 ha
- Eligible blocks (age class >= 40): 1000139
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 32.47 MB
- Schedules: 1.19 MB
- Runs: 0.00 MB
- Total: 33.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
