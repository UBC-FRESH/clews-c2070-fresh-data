# WS4 tiled 30-m dataset — J33|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J33|NL|S22` (parent `J33|NL`)
- Tile / row / col: `J33` / 2 / 2
- Province: `NL`
- Centroid: 51.140788, -56.456519
- Allocated harvest: 7218.504736 m3
- Productive subcell area: 152495.490952 ha
- Committed geometry area: 229808.105781 ha
- Clipped inventory geometry: 229808.105781 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1662943
- Blocks: 935880
- Forest area: 149664.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 87775
- Scheduled area: 13215.78 ha
- Eligible blocks (age class >= 40): 877744
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.71 MB
- Schedules: 1.04 MB
- Runs: 0.00 MB
- Total: 25.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
