# WS4 tiled 30-m dataset — K26|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K26|QC|S12` (parent `K26|QC`)
- Tile / row / col: `K26` / 1 / 2
- Province: `QC`
- Centroid: 56.571219, -69.995832
- Allocated harvest: 21934.268040 m3
- Productive subcell area: 125636.071965 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1154976
- Blocks: 547957
- Forest area: 103947.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 40919
- Scheduled area: 7657.83 ha
- Eligible blocks (age class >= 40): 409185
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.84 MB
- Schedules: 0.48 MB
- Runs: 0.00 MB
- Total: 16.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
