# WS4 tiled 30-m dataset — G19|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G19|ON|S12` (parent `G19|ON`)
- Tile / row / col: `G19` / 1 / 2
- Province: `ON`
- Centroid: 53.557156, -88.644655
- Allocated harvest: 14178.961437 m3
- Productive subcell area: 168654.852009 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2158582
- Blocks: 608784
- Forest area: 194272.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55557
- Scheduled area: 16235.73 ha
- Eligible blocks (age class >= 40): 555565
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.67 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 24.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
