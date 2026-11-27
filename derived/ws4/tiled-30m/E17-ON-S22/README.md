# WS4 tiled 30-m dataset — E17|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E17|ON|S22` (parent `E17|ON`)
- Tile / row / col: `E17` / 2 / 2
- Province: `ON`
- Centroid: 51.457881, -93.343772
- Allocated harvest: 40949.682342 m3
- Productive subcell area: 193617.098470 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1965625
- Blocks: 739132
- Forest area: 176906.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 64931
- Scheduled area: 14415.21 ha
- Eligible blocks (age class >= 40): 649302
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.34 MB
- Schedules: 0.77 MB
- Runs: 0.00 MB
- Total: 25.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
