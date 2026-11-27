# WS4 tiled 30-m dataset — G12|SK|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G12|SK|S11` (parent `G12|SK`)
- Tile / row / col: `G12` / 1 / 1
- Province: `SK`
- Centroid: 53.230145, -105.466849
- Allocated harvest: 32142.591788 m3
- Productive subcell area: 162615.589192 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 559357
- Blocks: 272986
- Forest area: 50342.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19768
- Scheduled area: 3784.59 ha
- Eligible blocks (age class >= 40): 197671
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.30 MB
- Schedules: 0.23 MB
- Runs: 0.00 MB
- Total: 8.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
