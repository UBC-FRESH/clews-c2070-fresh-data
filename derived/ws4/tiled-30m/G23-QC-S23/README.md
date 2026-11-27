# WS4 tiled 30-m dataset — G23|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G23|QC|S23` (parent `G23|QC`)
- Tile / row / col: `G23` / 2 / 3
- Province: `QC`
- Centroid: 52.970544, -78.648696
- Allocated harvest: 17711.783776 m3
- Productive subcell area: 97397.565492 ha
- Committed geometry area: 161140.738437 ha
- Clipped inventory geometry: 161140.738437 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1287653
- Blocks: 530971
- Forest area: 115888.77 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46761
- Scheduled area: 8712.99 ha
- Eligible blocks (age class >= 40): 467606
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.71 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 17.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
