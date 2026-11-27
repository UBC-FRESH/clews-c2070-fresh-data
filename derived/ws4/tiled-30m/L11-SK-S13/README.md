# WS4 tiled 30-m dataset — L11|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L11|SK|S13` (parent `L11|SK`)
- Tile / row / col: `L11` / 1 / 3
- Province: `SK`
- Centroid: 59.840867, -108.628468
- Allocated harvest: 12712.829385 m3
- Productive subcell area: 110121.349555 ha
- Committed geometry area: 175484.902186 ha
- Clipped inventory geometry: 175484.902186 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1414393
- Blocks: 237757
- Forest area: 127295.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12748
- Scheduled area: 3113.28 ha
- Eligible blocks (age class >= 40): 127478
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.69 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 12.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
