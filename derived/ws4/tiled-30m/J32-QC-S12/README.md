# WS4 tiled 30-m dataset — J32|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|QC|S12` (parent `J32|QC`)
- Tile / row / col: `J32` / 1 / 2
- Province: `QC`
- Centroid: 51.528871, -58.684065
- Allocated harvest: 35632.260728 m3
- Productive subcell area: 176450.076202 ha
- Committed geometry area: 248415.579794 ha
- Clipped inventory geometry: 248415.579794 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2139620
- Blocks: 691247
- Forest area: 192565.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65606
- Scheduled area: 18466.65 ha
- Eligible blocks (age class >= 40): 656060
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.21 MB
- Schedules: 0.78 MB
- Runs: 0.00 MB
- Total: 25.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
