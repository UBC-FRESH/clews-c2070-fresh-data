# WS4 tiled 30-m dataset — H33|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H33|NL|S22` (parent `H33|NL`)
- Tile / row / col: `H33` / 2 / 2
- Province: `NL`
- Centroid: 48.844811, -58.524666
- Allocated harvest: 1669.341725 m3
- Productive subcell area: 23990.790755 ha
- Committed geometry area: 34669.012866 ha
- Clipped inventory geometry: 34669.012866 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 239664
- Blocks: 125529
- Forest area: 21569.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11434
- Scheduled area: 2020.41 ha
- Eligible blocks (age class >= 40): 114337
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.32 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 4.45 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
