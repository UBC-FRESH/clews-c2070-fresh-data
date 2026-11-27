# WS4 tiled 30-m dataset — D30|NB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D30|NB|S33` (parent `D30|NB`)
- Tile / row / col: `D30` / 3 / 3
- Province: `NB`
- Centroid: 46.315910, -66.958187
- Allocated harvest: 211115.818464 m3
- Productive subcell area: 218747.429711 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2652641
- Blocks: 937240
- Forest area: 238737.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75764
- Scheduled area: 14310.81 ha
- Eligible blocks (age class >= 40): 757639
- Simulated years: 20
- Harvested volume: 2584992.326 m3
- Treated/managed area: 14310.810 ha

## Storage

- Dataset: 31.68 MB
- Schedules: 0.90 MB
- Runs: 15.80 MB
- Total: 48.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
