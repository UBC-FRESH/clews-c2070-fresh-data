# WS4 tiled 30-m dataset — C26|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C26|QC|S12` (parent `C26|QC`)
- Tile / row / col: `C26` / 1 / 2
- Province: `QC`
- Centroid: 46.336613, -75.908759
- Allocated harvest: 127938.356993 m3
- Productive subcell area: 207690.437894 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2263024
- Blocks: 647806
- Forest area: 203672.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60097
- Scheduled area: 18422.82 ha
- Eligible blocks (age class >= 40): 600963
- Simulated years: 20
- Harvested volume: 4064796.268 m3
- Treated/managed area: 18422.820 ha

## Storage

- Dataset: 25.83 MB
- Schedules: 0.71 MB
- Runs: 19.87 MB
- Total: 46.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
