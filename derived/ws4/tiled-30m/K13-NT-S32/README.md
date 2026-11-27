# WS4 tiled 30-m dataset — K13|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K13|NT|S32` (parent `K13|NT`)
- Tile / row / col: `K13` / 3 / 2
- Province: `NT`
- Centroid: 60.047721, -103.946523
- Allocated harvest: 14.210589 m3
- Productive subcell area: 26192.570505 ha
- Committed geometry area: 49579.187173 ha
- Clipped inventory geometry: 49579.187173 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 306645
- Blocks: 73897
- Forest area: 27598.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5955
- Scheduled area: 1148.67 ha
- Eligible blocks (age class >= 40): 59547
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.49 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
