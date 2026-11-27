# WS4 tiled 30-m dataset — I13|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I13|SK|S33` (parent `I13|SK`)
- Tile / row / col: `I13` / 3 / 3
- Province: `SK`
- Centroid: 57.182416, -102.414229
- Allocated harvest: 26445.022681 m3
- Productive subcell area: 165119.592567 ha
- Committed geometry area: 241111.657509 ha
- Clipped inventory geometry: 241111.657509 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 910830
- Blocks: 215097
- Forest area: 81974.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17616
- Scheduled area: 5975.28 ha
- Eligible blocks (age class >= 40): 176158
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.41 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 9.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
