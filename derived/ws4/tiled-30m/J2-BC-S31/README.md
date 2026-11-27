# WS4 tiled 30-m dataset — J2|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J2|BC|S31` (parent `J2|BC`)
- Tile / row / col: `J2` / 3 / 1
- Province: `BC`
- Centroid: 53.259966, -129.918847
- Allocated harvest: 43761.271658 m3
- Productive subcell area: 57685.998827 ha
- Committed geometry area: 79005.794876 ha
- Clipped inventory geometry: 79005.794876 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 805253
- Blocks: 421077
- Forest area: 72472.77 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41708
- Scheduled area: 7195.86 ha
- Eligible blocks (age class >= 40): 417075
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.90 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 12.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
