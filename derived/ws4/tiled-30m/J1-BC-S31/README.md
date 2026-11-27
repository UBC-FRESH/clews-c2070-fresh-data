# WS4 tiled 30-m dataset — J1|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J1|BC|S31` (parent `J1|BC`)
- Tile / row / col: `J1` / 3 / 1
- Province: `BC`
- Centroid: 52.504636, -131.606609
- Allocated harvest: 65387.842594 m3
- Productive subcell area: 65214.172641 ha
- Committed geometry area: 67845.071478 ha
- Clipped inventory geometry: 67845.071478 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 702342
- Blocks: 369853
- Forest area: 63210.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36491
- Scheduled area: 6166.44 ha
- Eligible blocks (age class >= 40): 364903
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.51 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 10.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
