# WS4 tiled 30-m dataset — E28|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E28|QC|S31` (parent `E28|QC`)
- Tile / row / col: `E28` / 3 / 1
- Province: `QC`
- Centroid: 48.970818, -71.027241
- Allocated harvest: 103517.441804 m3
- Productive subcell area: 212624.115112 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2389334
- Blocks: 850333
- Forest area: 215040.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73828
- Scheduled area: 17447.58 ha
- Eligible blocks (age class >= 40): 738276
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.40 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 30.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
