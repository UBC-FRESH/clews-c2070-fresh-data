# WS4 tiled 30-m dataset — L11|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L11|NT|S22` (parent `L11|NT`)
- Tile / row / col: `L11` / 2 / 2
- Province: `NT`
- Centroid: 60.258722, -109.738326
- Allocated harvest: 105.992555 m3
- Productive subcell area: 149519.458329 ha
- Committed geometry area: 248890.910607 ha
- Clipped inventory geometry: 248890.910607 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2057535
- Blocks: 295769
- Forest area: 185178.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14487
- Scheduled area: 4650.03 ha
- Eligible blocks (age class >= 40): 144861
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.19 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 17.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
