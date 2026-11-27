# WS4 tiled 30-m dataset — H13|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H13|MB|S13` (parent `H13|MB`)
- Tile / row / col: `H13` / 1 / 3
- Province: `MB`
- Centroid: 54.909198, -101.710911
- Allocated harvest: 3055.540807 m3
- Productive subcell area: 78110.535930 ha
- Committed geometry area: 106566.005104 ha
- Clipped inventory geometry: 106566.005104 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 419533
- Blocks: 135798
- Forest area: 37757.97 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10653
- Scheduled area: 1907.37 ha
- Eligible blocks (age class >= 40): 106529
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.46 MB
- Schedules: 0.12 MB
- Runs: 0.00 MB
- Total: 5.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
