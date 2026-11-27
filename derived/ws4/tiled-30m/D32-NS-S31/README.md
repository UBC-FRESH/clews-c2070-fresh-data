# WS4 tiled 30-m dataset — D32|NS|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D32|NS|S31` (parent `D32|NS`)
- Tile / row / col: `D32` / 3 / 1
- Province: `NS`
- Centroid: 45.497644, -64.573449
- Allocated harvest: 51077.664463 m3
- Productive subcell area: 88327.724335 ha
- Committed geometry area: 108466.037612 ha
- Clipped inventory geometry: 108466.037612 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1084310
- Blocks: 299517
- Forest area: 97587.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24696
- Scheduled area: 7466.67 ha
- Eligible blocks (age class >= 40): 246953
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.32 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 12.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
