# WS4 tiled 30-m dataset — Q5|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q5|YT|S31` (parent `Q5|YT`)
- Tile / row / col: `Q5` / 3 / 1
- Province: `YT`
- Centroid: 63.524452, -133.243808
- Allocated harvest: 172.431229 m3
- Productive subcell area: 153753.487628 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2290784
- Blocks: 683030
- Forest area: 206170.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60603
- Scheduled area: 15741.72 ha
- Eligible blocks (age class >= 40): 606029
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.74 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 26.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
