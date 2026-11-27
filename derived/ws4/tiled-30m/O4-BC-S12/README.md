# WS4 tiled 30-m dataset — O4|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O4|BC|S12` (parent `O4|BC`)
- Tile / row / col: `O4` / 1 / 2
- Province: `BC`
- Centroid: 59.855272, -130.593745
- Allocated harvest: 17156.480928 m3
- Productive subcell area: 94888.446823 ha
- Committed geometry area: 173910.659438 ha
- Clipped inventory geometry: 173910.659438 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 993188
- Blocks: 605136
- Forest area: 89386.92 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55102
- Scheduled area: 7905.06 ha
- Eligible blocks (age class >= 40): 551014
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.39 MB
- Schedules: 0.65 MB
- Runs: 0.00 MB
- Total: 16.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
