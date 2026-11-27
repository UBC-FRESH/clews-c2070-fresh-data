# WS4 tiled 30-m dataset — J14|SK|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J14|SK|S31` (parent `J14|SK`)
- Tile / row / col: `J14` / 3 / 1
- Province: `SK`
- Centroid: 58.599780, -102.138575
- Allocated harvest: 3633.355487 m3
- Productive subcell area: 42756.109720 ha
- Committed geometry area: 74576.248504 ha
- Clipped inventory geometry: 74576.248504 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 468834
- Blocks: 108719
- Forest area: 42195.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7967
- Scheduled area: 2007.99 ha
- Eligible blocks (age class >= 40): 79664
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.24 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 5.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
