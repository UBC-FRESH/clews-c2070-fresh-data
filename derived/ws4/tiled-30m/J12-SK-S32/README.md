# WS4 tiled 30-m dataset — J12|SK|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J12|SK|S32` (parent `J12|SK`)
- Tile / row / col: `J12` / 3 / 2
- Province: `SK`
- Centroid: 58.278023, -106.180032
- Allocated harvest: 12476.833742 m3
- Productive subcell area: 143243.759432 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1630953
- Blocks: 321663
- Forest area: 146785.77 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16094
- Scheduled area: 2896.56 ha
- Eligible blocks (age class >= 40): 160940
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.39 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 15.57 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
