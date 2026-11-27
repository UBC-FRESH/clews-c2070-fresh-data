# WS4 tiled 30-m dataset — G12|SK|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G12|SK|S32` (parent `G12|SK`)
- Tile / row / col: `G12` / 3 / 2
- Province: `SK`
- Centroid: 54.204073, -104.953319
- Allocated harvest: 32142.591788 m3
- Productive subcell area: 162615.589192 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 825694
- Blocks: 296460
- Forest area: 74312.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26207
- Scheduled area: 5589.00 ha
- Eligible blocks (age class >= 40): 262064
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.37 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 10.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
