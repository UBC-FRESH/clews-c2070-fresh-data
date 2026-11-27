# WS4 tiled 30-m dataset — G31|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G31|QC|S31` (parent `G31|QC`)
- Tile / row / col: `G31` / 3 / 1
- Province: `QC`
- Centroid: 49.695846, -63.616868
- Allocated harvest: 63505.730344 m3
- Productive subcell area: 141442.665346 ha
- Committed geometry area: 166015.235661 ha
- Clipped inventory geometry: 166015.235661 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1682508
- Blocks: 687391
- Forest area: 151425.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 64455
- Scheduled area: 12486.33 ha
- Eligible blocks (age class >= 40): 644549
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.66 MB
- Schedules: 0.76 MB
- Runs: 0.00 MB
- Total: 22.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
