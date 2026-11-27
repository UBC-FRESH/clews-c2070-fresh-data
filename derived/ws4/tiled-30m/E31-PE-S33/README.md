# WS4 tiled 30-m dataset — E31|PE|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E31|PE|S33` (parent `E31|PE`)
- Tile / row / col: `E31` / 3 / 3
- Province: `PE`
- Centroid: 46.812681, -64.182030
- Allocated harvest: 48127.767591 m3
- Productive subcell area: 36616.670914 ha
- Committed geometry area: 63756.089891 ha
- Clipped inventory geometry: 63756.089891 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 350615
- Blocks: 134789
- Forest area: 31555.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9751
- Scheduled area: 2111.76 ha
- Eligible blocks (age class >= 40): 97506
- Simulated years: 20
- Harvested volume: 335026.606 m3
- Treated/managed area: 2111.760 ha

## Storage

- Dataset: 5.17 MB
- Schedules: 0.11 MB
- Runs: 2.31 MB
- Total: 7.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
