# WS4 tiled 30-m dataset — H2|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H2|BC|S22` (parent `H2|BC`)
- Tile / row / col: `H2` / 2 / 2
- Province: `BC`
- Centroid: 50.486539, -126.811424
- Allocated harvest: 100528.670659 m3
- Productive subcell area: 114575.684661 ha
- Committed geometry area: 138060.897904 ha
- Clipped inventory geometry: 138060.897904 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1472740
- Blocks: 560823
- Forest area: 132546.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 54900
- Scheduled area: 9916.11 ha
- Eligible blocks (age class >= 40): 548995
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.05 MB
- Schedules: 0.65 MB
- Runs: 0.00 MB
- Total: 18.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
