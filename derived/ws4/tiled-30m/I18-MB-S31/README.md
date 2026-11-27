# WS4 tiled 30-m dataset — I18|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I18|MB|S31` (parent `I18|MB`)
- Tile / row / col: `I18` / 3 / 1
- Province: `MB`
- Centroid: 57.177955, -91.188361
- Allocated harvest: 273.900797 m3
- Productive subcell area: 21164.703671 ha
- Committed geometry area: 39335.987004 ha
- Clipped inventory geometry: 39335.987004 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 273779
- Blocks: 86423
- Forest area: 24640.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7637
- Scheduled area: 1991.79 ha
- Eligible blocks (age class >= 40): 76363
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.69 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 3.77 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
