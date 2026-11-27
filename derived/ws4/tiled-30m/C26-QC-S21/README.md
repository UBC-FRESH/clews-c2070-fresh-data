# WS4 tiled 30-m dataset — C26|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C26|QC|S21` (parent `C26|QC`)
- Tile / row / col: `C26` / 2 / 1
- Province: `QC`
- Centroid: 46.892753, -76.337813
- Allocated harvest: 127938.356993 m3
- Productive subcell area: 207690.437894 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2431663
- Blocks: 675278
- Forest area: 218849.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 61535
- Scheduled area: 18832.32 ha
- Eligible blocks (age class >= 40): 615343
- Simulated years: 20
- Harvested volume: 4089903.444 m3
- Treated/managed area: 18832.320 ha

## Storage

- Dataset: 27.31 MB
- Schedules: 0.73 MB
- Runs: 20.34 MB
- Total: 48.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
