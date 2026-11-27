# WS4 tiled 30-m dataset — F31|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F31|QC|S32` (parent `F31|QC`)
- Tile / row / col: `F31` / 3 / 2
- Province: `QC`
- Centroid: 48.494266, -64.161754
- Allocated harvest: 581.628955 m3
- Productive subcell area: 1166.044944 ha
- Committed geometry area: 1242.441251 ha
- Clipped inventory geometry: 1242.441251 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 9777
- Blocks: 5210
- Forest area: 879.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4667
- Scheduled area: 790.74 ha
- Eligible blocks (age class >= 40): 4667
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.25 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 0.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
