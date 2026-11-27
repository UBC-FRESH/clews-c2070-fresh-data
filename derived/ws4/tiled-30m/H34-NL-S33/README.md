# WS4 tiled 30-m dataset — H34|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H34|NL|S33` (parent `H34|NL`)
- Tile / row / col: `H34` / 3 / 3
- Province: `NL`
- Centroid: 48.269906, -56.179163
- Allocated harvest: 7633.462120 m3
- Productive subcell area: 125945.739779 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1440621
- Blocks: 842320
- Forest area: 129655.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73811
- Scheduled area: 11407.95 ha
- Eligible blocks (age class >= 40): 738106
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.06 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 22.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
