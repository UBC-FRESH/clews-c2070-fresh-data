# WS4 tiled 30-m dataset — J6|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J6|BC|S31` (parent `J6|BC`)
- Tile / row / col: `J6` / 3 / 1
- Province: `BC`
- Centroid: 55.708736, -121.520967
- Allocated harvest: 118034.013691 m3
- Productive subcell area: 209725.032340 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2493548
- Blocks: 940590
- Forest area: 224419.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 88380
- Scheduled area: 19821.42 ha
- Eligible blocks (age class >= 40): 883794
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.14 MB
- Schedules: 1.05 MB
- Runs: 0.00 MB
- Total: 32.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
