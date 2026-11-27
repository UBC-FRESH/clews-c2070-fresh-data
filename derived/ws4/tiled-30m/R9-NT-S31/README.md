# WS4 tiled 30-m dataset — R9|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R9|NT|S31` (parent `R9|NT`)
- Tile / row / col: `R9` / 3 / 1
- Province: `NT`
- Centroid: 67.510417, -123.318436
- Allocated harvest: 2.492509 m3
- Productive subcell area: 6703.253447 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1349688
- Blocks: 497942
- Forest area: 121471.92 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38507
- Scheduled area: 9882.99 ha
- Eligible blocks (age class >= 40): 385070
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.80 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 17.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
