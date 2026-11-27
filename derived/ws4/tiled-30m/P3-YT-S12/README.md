# WS4 tiled 30-m dataset — P3|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P3|YT|S12` (parent `P3|YT`)
- Tile / row / col: `P3` / 1 / 2
- Province: `YT`
- Centroid: 60.305157, -134.448788
- Allocated harvest: 293.966653 m3
- Productive subcell area: 164998.347871 ha
- Committed geometry area: 249612.545773 ha
- Clipped inventory geometry: 249612.545773 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2056527
- Blocks: 932316
- Forest area: 185087.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 86531
- Scheduled area: 17201.97 ha
- Eligible blocks (age class >= 40): 865309
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.64 MB
- Schedules: 1.03 MB
- Runs: 0.00 MB
- Total: 28.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
