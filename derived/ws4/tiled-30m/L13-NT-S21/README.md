# WS4 tiled 30-m dataset — L13|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L13|NT|S21` (parent `L13|NT`)
- Tile / row / col: `L13` / 2 / 1
- Province: `NT`
- Centroid: 60.706811, -105.147792
- Allocated harvest: 40.712733 m3
- Productive subcell area: 104674.290360 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1380245
- Blocks: 439749
- Forest area: 124222.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37323
- Scheduled area: 24156.72 ha
- Eligible blocks (age class >= 40): 373229
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.74 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 16.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
