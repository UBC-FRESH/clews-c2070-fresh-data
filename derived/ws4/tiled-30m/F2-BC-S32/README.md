# WS4 tiled 30-m dataset — F2|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F2|BC|S32` (parent `F2|BC`)
- Tile / row / col: `F2` / 3 / 2
- Province: `BC`
- Centroid: 48.769134, -124.912579
- Allocated harvest: 61339.524716 m3
- Productive subcell area: 63823.992894 ha
- Committed geometry area: 68840.254088 ha
- Clipped inventory geometry: 68840.254088 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 713024
- Blocks: 245970
- Forest area: 64172.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24057
- Scheduled area: 4527.45 ha
- Eligible blocks (age class >= 40): 240561
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.66 MB
- Schedules: 0.28 MB
- Runs: 0.00 MB
- Total: 8.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
