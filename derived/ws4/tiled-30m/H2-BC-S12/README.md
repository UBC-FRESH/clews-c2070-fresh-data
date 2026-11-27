# WS4 tiled 30-m dataset — H2|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H2|BC|S12` (parent `H2|BC`)
- Tile / row / col: `H2` / 1 / 2
- Province: `BC`
- Centroid: 50.227619, -126.327487
- Allocated harvest: 178335.001987 m3
- Productive subcell area: 203254.005229 ha
- Committed geometry area: 244916.105434 ha
- Clipped inventory geometry: 244916.105434 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2513274
- Blocks: 726580
- Forest area: 226194.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69904
- Scheduled area: 15212.88 ha
- Eligible blocks (age class >= 40): 699031
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.19 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 28.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
