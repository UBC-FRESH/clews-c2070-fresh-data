# WS4 tiled 30-m dataset — N13|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N13|NT|S22` (parent `N13|NT`)
- Tile / row / col: `N13` / 2 / 2
- Province: `NT`
- Centroid: 63.519551, -105.112448
- Allocated harvest: 2.312004 m3
- Productive subcell area: 6489.910079 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 47632
- Blocks: 32110
- Forest area: 4286.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1196
- Scheduled area: 148.23 ha
- Eligible blocks (age class >= 40): 11959
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.04 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
