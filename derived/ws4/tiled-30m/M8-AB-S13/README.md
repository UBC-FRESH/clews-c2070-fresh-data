# WS4 tiled 30-m dataset — M8|AB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M8|AB|S13` (parent `M8|AB`)
- Tile / row / col: `M8` / 1 / 3
- Province: `AB`
- Centroid: 59.923855, -117.358288
- Allocated harvest: 14583.633998 m3
- Productive subcell area: 38540.763858 ha
- Committed geometry area: 79736.774445 ha
- Clipped inventory geometry: 79736.774445 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 458537
- Blocks: 154557
- Forest area: 41268.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11190
- Scheduled area: 1981.44 ha
- Eligible blocks (age class >= 40): 111891
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.98 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 6.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
