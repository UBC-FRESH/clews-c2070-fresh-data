# WS4 tiled 30-m dataset — O4|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O4|BC|S13` (parent `O4|BC`)
- Tile / row / col: `O4` / 1 / 3
- Province: `BC`
- Centroid: 59.949999, -129.862630
- Allocated harvest: 2962.393274 m3
- Productive subcell area: 16384.298028 ha
- Committed geometry area: 30028.988457 ha
- Clipped inventory geometry: 30028.988457 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 320747
- Blocks: 176013
- Forest area: 28867.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17228
- Scheduled area: 2756.34 ha
- Eligible blocks (age class >= 40): 172276
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.55 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 5.75 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
