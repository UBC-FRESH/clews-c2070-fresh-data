# WS4 tiled 30-m dataset — G3|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G3|BC|S32` (parent `G3|BC`)
- Tile / row / col: `G3` / 3 / 2
- Province: `BC`
- Centroid: 50.451089, -124.115920
- Allocated harvest: 153382.673787 m3
- Productive subcell area: 175803.096591 ha
- Committed geometry area: 247411.231944 ha
- Clipped inventory geometry: 247411.231944 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1246548
- Blocks: 771948
- Forest area: 112189.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 70236
- Scheduled area: 9309.42 ha
- Eligible blocks (age class >= 40): 702358
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.57 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 20.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
