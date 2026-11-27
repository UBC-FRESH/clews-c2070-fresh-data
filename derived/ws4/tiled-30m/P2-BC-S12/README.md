# WS4 tiled 30-m dataset — P2|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P2|BC|S12` (parent `P2|BC`)
- Tile / row / col: `P2` / 1 / 2
- Province: `BC`
- Centroid: 59.490479, -136.730467
- Allocated harvest: 8108.767238 m3
- Productive subcell area: 25052.703241 ha
- Committed geometry area: 212457.050126 ha
- Clipped inventory geometry: 212457.050126 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 128185
- Blocks: 84992
- Forest area: 11536.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7054
- Scheduled area: 907.83 ha
- Eligible blocks (age class >= 40): 70539
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.78 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 2.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
