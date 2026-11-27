# WS4 tiled 30-m dataset — H4|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H4|BC|S31` (parent `H4|BC`)
- Tile / row / col: `H4` / 3 / 1
- Province: `BC`
- Centroid: 52.070414, -123.774124
- Allocated harvest: 122645.043058 m3
- Productive subcell area: 203257.105769 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2479602
- Blocks: 669847
- Forest area: 223164.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59598
- Scheduled area: 13296.69 ha
- Eligible blocks (age class >= 40): 595980
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.26 MB
- Schedules: 0.70 MB
- Runs: 0.00 MB
- Total: 26.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
