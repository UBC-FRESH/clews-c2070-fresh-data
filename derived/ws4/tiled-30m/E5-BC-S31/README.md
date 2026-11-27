# WS4 tiled 30-m dataset — E5|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E5|BC|S31` (parent `E5|BC`)
- Tile / row / col: `E5` / 3 / 1
- Province: `BC`
- Centroid: 49.064689, -119.254028
- Allocated harvest: 44626.955086 m3
- Productive subcell area: 53411.471020 ha
- Committed geometry area: 63683.793676 ha
- Clipped inventory geometry: 63683.793676 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 428227
- Blocks: 212641
- Forest area: 38540.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17913
- Scheduled area: 2690.82 ha
- Eligible blocks (age class >= 40): 179130
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.72 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 6.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
