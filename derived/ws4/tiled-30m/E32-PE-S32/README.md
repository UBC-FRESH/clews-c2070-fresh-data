# WS4 tiled 30-m dataset — E32|PE|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|PE|S32` (parent `E32|PE`)
- Tile / row / col: `E32` / 3 / 2
- Province: `PE`
- Centroid: 46.375997, -63.292472
- Allocated harvest: 44990.615644 m3
- Productive subcell area: 41634.338216 ha
- Committed geometry area: 92268.787069 ha
- Clipped inventory geometry: 92268.787069 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 307679
- Blocks: 153280
- Forest area: 27691.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9983
- Scheduled area: 1807.83 ha
- Eligible blocks (age class >= 40): 99828
- Simulated years: 20
- Harvested volume: 239056.759 m3
- Treated/managed area: 1807.830 ha

## Storage

- Dataset: 5.13 MB
- Schedules: 0.11 MB
- Runs: 2.00 MB
- Total: 7.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
