# WS4 tiled 30-m dataset — K3|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K3|BC|S11` (parent `K3|BC`)
- Tile / row / col: `K3` / 1 / 1
- Province: `BC`
- Centroid: 54.248870, -128.271114
- Allocated harvest: 110195.225817 m3
- Productive subcell area: 187783.516740 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2138124
- Blocks: 967090
- Forest area: 192431.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 92587
- Scheduled area: 15595.83 ha
- Eligible blocks (age class >= 40): 925866
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.71 MB
- Schedules: 1.10 MB
- Runs: 0.00 MB
- Total: 28.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
