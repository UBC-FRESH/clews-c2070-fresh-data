# WS4 tiled 30-m dataset — B27|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B27|QC|S31` (parent `B27|QC`)
- Tile / row / col: `B27` / 3 / 1
- Province: `QC`
- Centroid: 45.737627, -74.890302
- Allocated harvest: 19908.349188 m3
- Productive subcell area: 30717.490720 ha
- Committed geometry area: 141333.656530 ha
- Clipped inventory geometry: 141333.656530 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1170171
- Blocks: 329973
- Forest area: 105315.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28884
- Scheduled area: 9451.44 ha
- Eligible blocks (age class >= 40): 288833
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.58 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 13.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
