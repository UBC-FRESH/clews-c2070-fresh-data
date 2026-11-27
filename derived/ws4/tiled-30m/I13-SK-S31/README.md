# WS4 tiled 30-m dataset — I13|SK|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I13|SK|S31` (parent `I13|SK`)
- Tile / row / col: `I13` / 3 / 1
- Province: `SK`
- Centroid: 57.060557, -104.075279
- Allocated harvest: 27419.892255 m3
- Productive subcell area: 171206.562836 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2146057
- Blocks: 264045
- Forest area: 193145.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21208
- Scheduled area: 13441.95 ha
- Eligible blocks (age class >= 40): 212078
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.57 MB
- Schedules: 0.25 MB
- Runs: 0.00 MB
- Total: 17.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
