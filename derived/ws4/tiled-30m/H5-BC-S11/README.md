# WS4 tiled 30-m dataset — H5|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H5|BC|S11` (parent `H5|BC`)
- Tile / row / col: `H5` / 1 / 1
- Province: `BC`
- Centroid: 51.815675, -121.157090
- Allocated harvest: 152183.427452 m3
- Productive subcell area: 194399.889107 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2316314
- Blocks: 1025094
- Forest area: 208468.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 89229
- Scheduled area: 14584.77 ha
- Eligible blocks (age class >= 40): 892289
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.76 MB
- Schedules: 1.06 MB
- Runs: 0.00 MB
- Total: 31.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
