# WS4 tiled 30-m dataset — K29|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K29|QC|S12` (parent `K29|QC`)
- Tile / row / col: `K29` / 1 / 2
- Province: `QC`
- Centroid: 54.706729, -63.836244
- Allocated harvest: 1298.954769 m3
- Productive subcell area: 7889.308356 ha
- Committed geometry area: 16304.320881 ha
- Clipped inventory geometry: 16304.320881 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 85795
- Blocks: 52899
- Forest area: 7721.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4768
- Scheduled area: 693.63 ha
- Eligible blocks (age class >= 40): 47672
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.77 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 1.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
