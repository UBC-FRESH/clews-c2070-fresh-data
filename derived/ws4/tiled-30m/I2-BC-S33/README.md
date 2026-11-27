# WS4 tiled 30-m dataset — I2|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I2|BC|S33` (parent `I2|BC`)
- Tile / row / col: `I2` / 3 / 3
- Province: `BC`
- Centroid: 52.454935, -127.439997
- Allocated harvest: 104201.786127 m3
- Productive subcell area: 141622.820248 ha
- Committed geometry area: 208748.015510 ha
- Clipped inventory geometry: 208748.015510 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1674825
- Blocks: 969030
- Forest area: 150734.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 92736
- Scheduled area: 14146.11 ha
- Eligible blocks (age class >= 40): 927359
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.82 MB
- Schedules: 1.10 MB
- Runs: 0.00 MB
- Total: 25.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
