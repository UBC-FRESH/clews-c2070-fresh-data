# WS4 tiled 30-m dataset — L5|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L5|BC|S11` (parent `L5|BC`)
- Tile / row / col: `L5` / 1 / 1
- Province: `BC`
- Centroid: 56.772331, -125.174211
- Allocated harvest: 41098.525057 m3
- Productive subcell area: 153152.440818 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2294306
- Blocks: 900309
- Forest area: 206487.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 83669
- Scheduled area: 15709.23 ha
- Eligible blocks (age class >= 40): 836684
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.00 MB
- Schedules: 0.99 MB
- Runs: 0.00 MB
- Total: 30.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
