# WS4 tiled 30-m dataset — C26|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C26|QC|S11` (parent `C26|QC`)
- Tile / row / col: `C26` / 1 / 1
- Province: `QC`
- Centroid: 46.466115, -76.524103
- Allocated harvest: 127938.356993 m3
- Productive subcell area: 207690.437894 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2446016
- Blocks: 657104
- Forest area: 220141.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60714
- Scheduled area: 20239.29 ha
- Eligible blocks (age class >= 40): 607139
- Simulated years: 20
- Harvested volume: 4494731.882 m3
- Treated/managed area: 20239.290 ha

## Storage

- Dataset: 27.25 MB
- Schedules: 0.72 MB
- Runs: 21.79 MB
- Total: 49.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
