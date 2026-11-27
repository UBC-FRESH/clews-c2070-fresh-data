# WS4 tiled 30-m dataset — N2|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N2|BC|S13` (parent `N2|BC`)
- Tile / row / col: `N2` / 1 / 3
- Province: `BC`
- Centroid: 57.594635, -132.549984
- Allocated harvest: 3930.007714 m3
- Productive subcell area: 9673.173906 ha
- Committed geometry area: 45907.997681 ha
- Clipped inventory geometry: 45907.997681 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 224
- Blocks: 84
- Forest area: 20.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4
- Scheduled area: 0.81 ha
- Eligible blocks (age class >= 40): 4
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.07 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
