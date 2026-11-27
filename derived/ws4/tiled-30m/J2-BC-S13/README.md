# WS4 tiled 30-m dataset — J2|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J2|BC|S13` (parent `J2|BC`)
- Tile / row / col: `J2` / 1 / 3
- Province: `BC`
- Centroid: 52.835337, -127.786545
- Allocated harvest: 134206.413753 m3
- Productive subcell area: 176910.558880 ha
- Committed geometry area: 242293.790700 ha
- Clipped inventory geometry: 242293.790700 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1300924
- Blocks: 803199
- Forest area: 117083.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73912
- Scheduled area: 10647.99 ha
- Eligible blocks (age class >= 40): 739114
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.26 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 21.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
