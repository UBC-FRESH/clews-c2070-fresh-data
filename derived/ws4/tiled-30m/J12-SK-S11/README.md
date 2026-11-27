# WS4 tiled 30-m dataset — J12|SK|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J12|SK|S11` (parent `J12|SK`)
- Tile / row / col: `J12` / 1 / 1
- Province: `SK`
- Centroid: 57.289823, -106.719330
- Allocated harvest: 12476.833742 m3
- Productive subcell area: 143243.759432 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1446847
- Blocks: 210365
- Forest area: 130216.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12218
- Scheduled area: 4198.32 ha
- Eligible blocks (age class >= 40): 122176
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.53 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 12.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
