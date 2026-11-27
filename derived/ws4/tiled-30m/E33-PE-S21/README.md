# WS4 tiled 30-m dataset — E33|PE|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E33|PE|S21` (parent `E33|PE`)
- Tile / row / col: `E33` / 2 / 1
- Province: `PE`
- Centroid: 45.974970, -62.527376
- Allocated harvest: 52.170202 m3
- Productive subcell area: 47.424810 ha
- Committed geometry area: 95.445390 ha
- Clipped inventory geometry: 95.445390 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 253
- Blocks: 128
- Forest area: 22.77 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 88
- Scheduled area: 17.28 ha
- Eligible blocks (age class >= 40): 88
- Simulated years: 20
- Harvested volume: 1849.822 m3
- Treated/managed area: 17.280 ha

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.02 MB
- Total: 0.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
