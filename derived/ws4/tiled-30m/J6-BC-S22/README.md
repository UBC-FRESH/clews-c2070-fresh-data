# WS4 tiled 30-m dataset — J6|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J6|BC|S22` (parent `J6|BC`)
- Tile / row / col: `J6` / 2 / 2
- Province: `BC`
- Centroid: 55.471231, -120.461853
- Allocated harvest: 116746.724514 m3
- Productive subcell area: 207437.752972 ha
- Committed geometry area: 247273.478346 ha
- Clipped inventory geometry: 247273.478346 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2423465
- Blocks: 1037931
- Forest area: 218111.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 96131
- Scheduled area: 18385.20 ha
- Eligible blocks (age class >= 40): 961301
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.84 MB
- Schedules: 1.15 MB
- Runs: 0.00 MB
- Total: 32.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
