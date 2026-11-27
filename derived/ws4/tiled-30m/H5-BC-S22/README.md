# WS4 tiled 30-m dataset — H5|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H5|BC|S22` (parent `H5|BC`)
- Tile / row / col: `H5` / 2 / 2
- Province: `BC`
- Centroid: 52.413008, -120.772726
- Allocated harvest: 152183.427452 m3
- Productive subcell area: 194399.889107 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2116648
- Blocks: 940588
- Forest area: 190498.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 88016
- Scheduled area: 15628.23 ha
- Eligible blocks (age class >= 40): 880159
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.88 MB
- Schedules: 1.05 MB
- Runs: 0.00 MB
- Total: 28.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
