# WS4 tiled 30-m dataset — H1|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H1|BC|S23` (parent `H1|BC`)
- Tile / row / col: `H1` / 2 / 3
- Province: `BC`
- Centroid: 50.271014, -127.728926
- Allocated harvest: 82553.322145 m3
- Productive subcell area: 77395.433300 ha
- Committed geometry area: 81023.687943 ha
- Clipped inventory geometry: 81023.687943 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 883661
- Blocks: 376881
- Forest area: 79529.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37135
- Scheduled area: 6294.69 ha
- Eligible blocks (age class >= 40): 371344
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.45 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 11.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
