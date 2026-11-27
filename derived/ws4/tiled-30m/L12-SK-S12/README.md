# WS4 tiled 30-m dataset — L12|SK|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L12|SK|S12` (parent `L12|SK`)
- Tile / row / col: `L12` / 1 / 2
- Province: `SK`
- Centroid: 59.931011, -106.815467
- Allocated harvest: 3509.218907 m3
- Productive subcell area: 46449.061442 ha
- Committed geometry area: 74033.416985 ha
- Clipped inventory geometry: 74033.416985 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 514104
- Blocks: 154853
- Forest area: 46269.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11314
- Scheduled area: 2074.77 ha
- Eligible blocks (age class >= 40): 113138
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.22 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 6.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
