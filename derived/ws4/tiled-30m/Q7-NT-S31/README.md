# WS4 tiled 30-m dataset — Q7|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q7|NT|S31` (parent `Q7|NT`)
- Tile / row / col: `Q7` / 3 / 1
- Province: `NT`
- Centroid: 64.997159, -127.829078
- Allocated harvest: 140.807692 m3
- Productive subcell area: 144411.735102 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 564325
- Blocks: 237469
- Forest area: 50789.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15920
- Scheduled area: 2834.10 ha
- Eligible blocks (age class >= 40): 159195
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.71 MB
- Schedules: 0.18 MB
- Runs: 0.00 MB
- Total: 7.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
