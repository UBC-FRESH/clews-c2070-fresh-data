# WS4 tiled 30-m dataset — L12|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L12|NT|S13` (parent `L12|NT`)
- Tile / row / col: `L12` / 1 / 3
- Province: `NT`
- Centroid: 60.202158, -105.909842
- Allocated harvest: 53.410634 m3
- Productive subcell area: 119290.029747 ha
- Committed geometry area: 220949.286623 ha
- Clipped inventory geometry: 220949.286623 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1291627
- Blocks: 487339
- Forest area: 116246.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42195
- Scheduled area: 8524.80 ha
- Eligible blocks (age class >= 40): 421942
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.12 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 16.62 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
