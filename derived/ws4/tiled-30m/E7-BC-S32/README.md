# WS4 tiled 30-m dataset — E7|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E7|BC|S32` (parent `E7|BC`)
- Tile / row / col: `E7` / 3 / 2
- Province: `BC`
- Centroid: 49.947421, -114.861002
- Allocated harvest: 84466.061544 m3
- Productive subcell area: 99491.570238 ha
- Committed geometry area: 132848.382716 ha
- Clipped inventory geometry: 132848.382716 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1072026
- Blocks: 545384
- Forest area: 96482.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47862
- Scheduled area: 7189.20 ha
- Eligible blocks (age class >= 40): 478619
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.40 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 15.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
